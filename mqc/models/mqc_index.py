# -*- coding: utf-8 -*-
from openerp import models, fields,api

class Index(models.Model):
    _name = "mqc.index" #index 医疗质量指标
    _description = u"医疗质量信息"
    _inherits = {'mqc.mqc': 'mqc_id'}
    mqc_id = fields.Many2one('mqc.mqc', u'报表id', required=True,
                              ondelete='cascade')
    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))
    _rec_name = 'year_month'

    #1、一般指标：
    outpat_capacity = fields.Integer(u'门诊量')
    discharged_case = fields.Integer(u'出院人数')
    accord_diag_case = fields.Float(u'出入院诊断符合率(%)')
    rescue_rate = fields.Float(u'抢救成功率(%)')
    avg_adm_days = fields.Integer(u'平均住院天数')
    bed_use_rate = fields.Float(u'床位使用率(%)')
    mr_grade_a_rate = fields.Float(u'甲级病案率(%)') #mr medical record
    #2、专项指标：
    opr_three_four = fields.Integer(u'四/三级手术率（三/二级医院）(%)')
    unplanned_opr_two = fields.Float(u'非计划二次手术率/例')
    antibiotics_use_rate = fields.Float(u'抗菌药物使用率/强度') #antibiotics抗生素
    cp_disease = fields.Float(u'临床路径开展病种数/例数') #cp clinic path

    #3、医疗纠纷情况：
    dispute_case = fields.Integer(u'纠纷投诉发生例数')
    attacked_case = fields.Float(u'医务人员受人身冲击数')

    #4、落实患者安全目标（是/否）：
    protect_pat1 = fields.Selection([('1', u'是'), ('0', u'否')],u'是否落实手术安全核查、风险评估、术者亲自沟通制度')
    protect_pat2 = fields.Selection([('1', u'是'), ('0', u'否')],u'是否有患者身份识别与手术部位标识')
    protect_pat3 = fields.Selection([('1', u'是'), ('0', u'否')],u'是否主动报告医疗隐患、医疗不良事件')

    # _sql_constraints = [
    #     ('year_month_uniq',
    #      'UNIQUE (year_month)',
    #      u'本月只能上报一次数据')
    # ]

    @api.multi
    def unlink(self):
        for index in self:
            index.mqc_id.unlink()
        return super(Index, self).unlink()


