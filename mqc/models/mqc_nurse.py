# -*- coding: utf-8 -*-
from odoo import models, fields,api

class Nurse(models.Model):
    _name = "mqc.nurse" #nurse 透析
    _description = u"护理质控"
    _inherits = {'mqc.mqc': 'mqc_id'}
    mqc_id = fields.Many2one('mqc.mqc', u'报表id', required=True,
                              ondelete='cascade')
    units_name = fields.Char(u'单位名称',
                             default=lambda self: self.env.user.company_id.name, )
    units_code = fields.Char(u'单位编码',
                             default=lambda self: self.env.user.company_id.units_code)
    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))
    _rec_name = 'year_month'

    nurse_detail = fields.One2many('mqc.nurse.detail','nurse_id', u'护理质控明细',copy=True)

    # _sql_constraints = [
    #     ('year_month_uniq',
    #      'UNIQUE (year_month)',
    #      u'本月只能上报一次数据')
    # ]
    @api.multi
    def unlink(self):
        for item in self:
            item.mqc_id.unlink()
        return super(Nurse, self).unlink()



class NurseDetail(models.Model):
    _name = 'mqc.nurse.detail'
    _description = u'护理质控明细'
    # company_id = fields.Many2one('res.company',u'单位名称')
    nurse_id = fields.Many2one('mqc.nurse',u'护理主记录', required=True,)
    units_name = fields.Char(u'单位名称',
                             default=lambda self: self.env.user.company_id.name, )
    units_code = fields.Char(u'单位编码',
                             default=lambda self: self.env.user.company_id.units_code)
    fct_bed_days = fields.Float(u'患者实际占用总床日数')
    bedsore_case = fields.Float(u'住院患者压疮发生总例数')
    inevitable_bedsore_case = fields.Integer(u'审核符合难免压疮例数') #inevitable难免
    predict_case= fields.Integer(u'院内预期压疮发生例数')
    unpredict_case= fields.Integer(u'院内非预期压疮发生例数') # unpredict非预期
    bring_in_case = fields.Integer(u'院外带入压疮例数')
    per_hundred_rate = fields.Float(u'每百张床上报不良事件 例次(%)')
    mis_inhaling = fields.Float(u'住院患者误吸发生率(‰)')
    wrong_dose_rate = fields.Float(u'给药错误发生例次（%）') #给药 dose
    fall_rate = fields.Float(u'住院患者跌倒发生率(‰)')
    unplanned_extubation = fields.Float(u'气管导管非计划性拔管发生率(‰)')

