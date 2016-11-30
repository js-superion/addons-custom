# -*- coding: utf-8 -*-
from openerp import models, fields,api

class Icu(models.Model):
    _name = "mqc.icu"
    _description = u"ICU填报"
    _inherits = {'mqc.mqc': 'mqc_id'}
    mqc_id = fields.Many2one('mqc.mqc', u'报表id', required=True,
                              ondelete='cascade')
    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))
    _rec_name = 'year_month'

    treated_rate = fields.Float(u'ICU 患者收治率(%)', )
    apache2_excess15 = fields.Float(u'急性生理与慢性健康评分（APACHE II 评分）≥15分患者收治率(%)', )
    joint_rounds = fields.Float(u'多学科联合查房率(%)', )
    exam_rate = fields.Float(u'抗菌药物治疗前病原学送检率(%)', )
    dvt_prevent = fields.Float(u'深静脉血栓（DVT）预防率(%)', )
    mortality = fields.Float(u'ICU 患者实际病死率(%)', )
    predict_mortality = fields.Float(u'ICU 患者预计病死率(%)', )
    std_mortality = fields.Float(u'ICU 症患者标化病死指数', )
    unplanned_extubation = fields.Float(u'非计划气管插管拔管率(%)', )
    intubation_within48h = fields.Float(u'气管插管拔管后48h内再插管率(%)', )
    return_within48h = fields.Float(u'转出ICU后48h内重返率(%)', )
    vpa_rate = fields.Float(u'呼吸机相关性肺炎（VAP）发病率(%)', )
    crbsi_rate = fields.Float(u'血管内导管相关血流感染（CRBSI）发病率(%)', )
    cauti_rate = fields.Float(u'导尿管相关泌尿系感染（CAUTI）发病率(%)', )

    # _sql_constraints = [
    #     ('year_month_uniq',
    #      'UNIQUE (year_month)',
    #      u'本月只能上报一次数据')
    # ]

    @api.multi
    def unlink(self):
        for icu in self:
            icu.mqc_id.unlink()
        return super(Icu, self).unlink()

