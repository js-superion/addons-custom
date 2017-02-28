# -*- coding: utf-8 -*-

from odoo import models, fields, api

class WentyRanger (models.Model):
    _name = 'wenty.range'
    _description = u'全国派送区域表'
    name = fields.Char(u'网点名称', required=True, index=True, copy=False, default='New')
    province = fields.Char(u'省')
    city = fields.Char(u'市')
    county = fields.Char( u'县区')
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
    name = fields.Char(u'订单号', required=True, index=True)
    #商品信息
    product_name = fields.Char(u'品名', required=True)
    spec = fields.Char(u'规格',)
    amount = fields.Float(u'数量',)
    charges = fields.Float(u'总金额',)
    #买家信息
    payment = fields.Float(u'支付金额', )
    receiver = fields.Char(u'收件人')
    receiver_phone = fields.Char(u'收件人手机')
    province = fields.Char(u'省')
    city = fields.Char(u'市')
    county = fields.Char( u'县区')
    street = fields.Char( u'街道')
    group_time = fields.Datetime(u'成团时间')

    #快递信息
    sender = fields.Char(u'发件人')
    sender_phone = fields.Char(u'发件人手机')
    promise_time = fields.Datetime(u'承诺发货时间')
    area_small = fields.Char(u'所属片区')
    area_manager = fields.Char(u'片区负责人')
    manager_phone = fields.Char(u'负责人电话')
    area_large = fields.Char(u'所属大区')
    area_province = fields.Char(u'所属省区')
    imp_date_time = fields.Datetime(u'导入时间')

