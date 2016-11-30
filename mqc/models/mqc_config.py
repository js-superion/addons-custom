# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.exceptions import ValidationError


class ResPartnerExt(models.Model):
     _inherit = 'res.company'
     units_code = fields.Char(u'单位编码', )


class Mqc(models.Model):
    _name = 'mqc.mqc'
    _description = u"医疗质控单位填报"
    company_id = fields.Many2one(
        'res.company',required=True,default=lambda self: self.env.user.company_id.id)
    units_code = fields.Char(u'单位编码',
                             default=lambda self: self.env.user.company_id.units_code)
    units_name = fields.Char(u'单位名称',
                             default=lambda self: self.env.user.company_id.name,)
    dept_name = fields.Char(u'上报科室',
                            default=lambda self: self.env.user.employee_ids.department_id.name,)
    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))
    # report_1 = fields.Many2one('mqc.blood.clinic',u'关联全院临床用血情况')
    # report_2 = fields.Many2one('mqc.blood.construct', u'关联输血科建设及检测技术')

    _sql_constraints = [
        ('unit_dept_month_uniq',
         'UNIQUE (year_month,units_name,dept_name)',
         u'本月只能上报一次数据')
    ]





class ConfigHospital(models.Model):
    _name = "mqc.hospital"
    _inherits = {'res.partner':'partner_id'}
    #关联到res_partner，级联删除
    partner_id = fields.Many2one(
        'res.partner',
        u'医院名称',required=True,
        ondelete ='cascade')
    hospital_code = fields.Char(
        u'平台编码',
        require=True,
    )

    @api.one
    @api.constrains('partner_id')
    def _check_hospital_id(self):
        domain = [
            ('partner_id', '=', self.partner_id),
        ]
        if len(self.search(domain)) > 1:
            raise ValidationError(u'医院名称不能重复')

    @api.one
    @api.constrains('hospital_code')
    def _check_hospital_code(self):
        domain = [
            ('hospital_code', '=', self.hospital_code),
        ]
        if len(self.search(domain)) > 1:
            raise ValidationError(u'医院编码不能重复')


class ConfigUser(models.Model):
    _name = "mqc.user"
    _inherits = {'res.partner':'user_id'}
    #关联到res_partner，级联删除
    user_id = fields.Many2one(
        'res.partner',
        u'用户名称的',required=True,
        ondelete ='cascade')
    user_code = fields.Char(
        u'平台编码',
        require=True,
    )
    user_phone= fields.Char(
        u'电话',
        related='user_id.phone',
        readonly=True,store=True,
    )
    user_fax = fields.Char(
        u'传真',
        related='user_id.fax',
        readonly=True, store=False,
    )


    @api.one
    @api.constrains('user_id')
    def _check_user_id(self):
        domain = [
            ('user_id', '=', self.user_id),
        ]
        if len(self.search(domain)) > 1:
            raise ValidationError(u'用户名称不能重复')

    @api.one
    @api.constrains('user_code')
    def _check_user_code(self):
        domain = [
            ('user_code', '=', self.user_code),
        ]
        if len(self.search(domain)) > 1:
            raise ValidationError(u'用户编码不能重复')

