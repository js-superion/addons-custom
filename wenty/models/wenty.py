# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class WentyRanger(models.Model):
    _name = 'wenty.range'
    _description = u'全国派送区域表'
    name = fields.Char(u'网点名称', required=True, index=True, copy=False, default='New')
    province = fields.Char(u'省')
    city = fields.Char(u'市')
    county = fields.Char(u'县区')
    partner_name = fields.Char(u'盟商姓名')
    phone = fields.Char(u'联系电话')
    in_range = fields.Char(u'派送范围')
    out_range = fields.Char(u'不派送范围')
    remark = fields.Char(u'备注')
    area_small = fields.Char(u'所属片区')
    area_manager = fields.Char(u'片区负责人')
    manager_phone = fields.Char(u'负责人电话')
    area_large = fields.Char(u'所属大区')
    area_province = fields.Char(u'所属省区')


class WentyOrder(models.Model):
    _name = 'wenty.order'
    _description = u'订单信息'

    # def _search_date_range(self, operator, value):
    #     if operator == 'like':
    #         operator = 'ilike'
    #     return [('name', operator, value)]

    name = fields.Char(u'订单号', required=True, index=True)
    create_date = fields.Datetime(u'导入时间')
    create_date_yy = fields.Char(string=u'日期缩写',compute='_compute_create_date_yy')
    # date_ranger = fields.Char(u'时间范围',compute='_compute_upper', search='_search_date_range')
    date_ranger = fields.Char(u'时间范围',)

    # @api.depends('date_ranger')
    # def _compute_upper(self):
    #     for rec in self:
    #         rec.date_ranger = '2019'


    #当过滤器查询时，调用
    @api.multi
    def _compute_create_date_yy(self):
        for order in self:
            dd = order.create_date
            yy_date = fields.Datetime.from_string(dd)
            # str_yy_date = yy_date.strftime('%y-%m-%d %H:%M:%S')
            str_yy_date = yy_date.strftime('%y-%m-%d %H:%M')
            order.create_date_yy = str_yy_date


    status = fields.Char(u'状态', default='0')
    # 商品信息
    product_name = fields.Char(u'品名', required=True)
    product_id = fields.Char(u'商品id',)
    spec = fields.Char(u'规格', )
    unit = fields.Char(u'单位', )
    amount = fields.Float(u'数量', )
    charges = fields.Float(u'总金额', )
    # 买家信息
    payment = fields.Float(u'支付金额', )
    receiver = fields.Char(u'收件人')
    receiver_phone = fields.Char(u'收件人手机')
    province = fields.Char(u'省')
    city = fields.Char(u'市')
    county = fields.Char(u'县区')
    street = fields.Char(u'街道')
    full_address = fields.Char(u'详细地址',)
    group_time = fields.Datetime(u'成团时间')

    # 快递信息
    sender = fields.Char(u'发件人')
    sender_phone = fields.Char(u'发件人手机')
    promise_time = fields.Datetime(u'承诺发货时间')
    area_small = fields.Char(u'所属片区')
    area_manager = fields.Char(u'片区负责人')
    manager_phone = fields.Char(u'负责人电话')
    area_large = fields.Char(u'所属大区')
    area_province = fields.Char(u'所属省区')
    imp_date_time = fields.Datetime(u'导入时间')

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        for index,value in enumerate(args):
            if value[0] in ('date_ranger',) and value[1] == "ilike":
                #判断是否含有分隔符
                if "-" not in value[2]:
                    raise ValidationError(_("两个日期中间请用 - 分割开"))
                date_begin, date_end = value[2].split('-')
                if not date_begin.isdigit() or not date_begin.isdigit():
                    raise ValidationError(_("请输入正确的日期格式"))
                current_year = fields.Date.from_string(fields.Date.today()).strftime('%Y')
                day_start = " 00:00:00"
                day_end = " 23:59:59"
                if len(date_begin) == 8:
                    date_begin += day_start
                if len(date_end) == 8:
                    date_end += day_end

                if len(date_begin) == 4:
                    date_begin = current_year + date_begin + day_start
                    if len(date_end) == 4:
                        date_end = current_year + date_end + day_end
                    elif len(date_end) == 6:
                        date_end = current_year[0:2] + date_end+ day_end

                elif len(date_begin) == 6:
                    date_begin = current_year[0:2] + date_begin+ day_start
                    if len(date_end) == 4:
                        date_end = current_year + date_end +  day_end
                    elif len(date_end) == 6:
                        date_end = current_year[0:2] + date_end+ day_end

                args+=[('create_date', '>=', date_begin), ('create_date', '<=', date_end)]
                del args[index]
        return super(WentyOrder, self).search(args, offset, limit, order, count=count)


    @api.multi
    def get_area_name(self):
        orders = self.browse(self.ids)
        for order in orders:

            ##取出省、市、县
            province = order.province
            city = order.city
            county = order.county
            street = order.street
            full_address = order.full_address
            area_small = order.area_small
            if province and city and county:
                #根据地址 找到 片区
                if not area_small:
                    deliver_range = self.env['wenty.range'].search(
                        [('province', '=', province), ('city', '=', city), ('county', '=', county)], limit=1)
                    # 更新片区
                    area_small = deliver_range.area_small
                    order.write({'area_small': deliver_range.area_small})
                if not  full_address:
                    # 生成详细地址，分2步，第一步把街道中含有的省、市、县区 清除，第二步再更更新
                    street_no_province = street.replace(province, '')
                    street_no_city = street_no_province.replace(city, '')
                    filted_street = street_no_city.replace(county, '')
                    full_address = province + city + "," + county + filted_street
                    order.write({'full_address': full_address})
                #两个都不为空，设置有效数据
                if full_address and area_small:
                    order.write({'status': '2'})
            else:
                #如果省、市、县区存在空的情况，status写为1、为无效数据
                order.write({'status': '1'})



