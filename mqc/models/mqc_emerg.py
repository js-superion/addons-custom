# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Emergency(models.Model):
    _name = "mqc.emergency"
    _inherits = {'mqc.mqc': 'mqc_id'}
    mqc_id = fields.Many2one('mqc.mqc', u'报表id', required=True,
                             ondelete='cascade')
    _description = u'急诊学科质控指标'
    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))
    _rec_name = 'year_month'
    # 一般信息 emerg,emergency 缩写

    # report_month = fields.Char(
    #     u'上报月份',
    # )

    emerg_case = fields.Integer(
        u'急诊病人数',
    )
    critical_case = fields.Integer(
        u'危重病抢救人数',
    )
    emerg_multiple  = fields.Integer(
        u'急诊多发伤病例数',
    )
    brain_case = fields.Integer(
        u'急诊脑外伤病例数',
    )
    shock_case = fields.Integer(
        u'急诊感染性休克病例数',
    )
    death_case = fields.Integer(
        u'危重病人死亡病例数',
    )
    infusion_case = fields.Integer(
        u'急诊输液人数',
    )
    eicu_case = fields.Integer(
        u'EICU住院病人数',
    )
    appache_case = fields.Integer(
        u'APPACHEⅡ评分>20的病例数',
    )
    eicu_avg_day = fields.Integer(
        u'EICU病人平均住院天数',
    )
    eicu_avg_cost = fields.Float(
        u'EICU出院患者平均住院费用',
    )
    poison_case = fields.Integer(
        u'中毒病例数',
    )
    alcoholism_case = fields.Integer(
        u'酒精中毒例数',
    )
    sedative_case = fields.Integer(
        u'镇静剂中毒例数',
    )
    mass_case = fields.Integer(
        u'群体性中毒事件（3例以上）（件）',
    )

    #有机磷农药中毒 yjl，有机磷 拼音缩写
    yjl_poison_case = fields.Integer(
        u'有机磷中毒病人数',
    )

    yjl_in_case = fields.Integer(
        u'住院病人数',
    )
    yjl_inout_confirm = fields.Integer(
        u'入出院诊断符合数',
    )
    yjl_cure_rate = fields.Float(
        u'治愈好转人率（%）',
    )
    yjl_death_case = fields.Integer(
        u'死亡病历数',
    )
    yjl_assist_breath = fields.Integer(
        u'辅助通气病例数',
    )
    blood_clean = fields.Integer(
        u'血液净化病例数',
    )
    reactivators_first_day = fields.Integer(
        u'重度患者首日复能剂平均使用量（g）',
    )
    reactivators_last_five = fields.Integer(
        u'复能剂使用时间>5天例数',
    )
    yjl_avg_days = fields.Integer(
        u'出院者平均住院天数',
    )
    yjl_avg_cost = fields.Integer(
        u'出院者平均住院费用',
    )

    # 百草枯中毒 bck,缩写
    bck_poison_case = fields.Integer(
        u'百草枯中毒病人数',
    )
    bck_in_case = fields.Integer(
        u'住院病人数',
    )
    bck_inout_confirm = fields.Integer(
        u'入出院诊断符合数',
    )
    bck_cure_rate = fields.Integer(
        u'好转率(%)',
    )
    bck_death_case = fields.Integer(
        u'死亡病例数',
    )
    lavage_case = fields.Integer(
        u'口服中毒患者白陶土洗胃例数',
    )
    bck_assist_breath = fields.Integer(
        u'辅助通气人数',
    )
    perfusion_rate = fields.Integer(
        u'血液灌流率(%)',
    )
    perfusion_within_four = fields.Integer(
        u'血液灌流距中毒时间≤4小时例数',
    )
    perfusion_excess4_h = fields.Integer(
        u'血液灌流距中毒时间>4小时例数',
    )
    perfusion_excess1_h = fields.Integer(
        u'血液灌流时间距就诊时间＞1小时例数',
    )
    glucocorticoid_case = fields.Integer(
        u'糖皮质激素使用例数',
    )
    depressor_case = fields.Integer(
        u'免疫抑制剂使用例数',
    )
    bck_avg_day = fields.Integer(
        u'出院者平均住院天数',
    )
    bck_avg_cost = fields.Integer(
        u'出院者平均住院费用',
    )

    # CPR术
    cpr_case = fields.Integer(
        u'CPR病例数',
    )
    cpr_in_hos = fields.Integer(
        u'院内CPR病例数',
    )
    cpr_before_hos = fields.Integer(
        u'院前CPR病例数',
    )
    self_rescue = fields.Integer(
        u'自主循环恢复例数',
    )
    cpc_one_two = fields.Integer(
        u'脑功能分级（CPC）1，2级病例数',
    )
    low_fever_case = fields.Integer(
        u'开展亚低温（32-35℃）病例数',
    )
    cpr_within3_min = fields.Integer(
        u'院内CPR除颤开始时间≤3分钟的病例数',
    )
    cpr_excess3_min = fields.Integer(
        u'院内CPR除颤开始时间>3分钟的病例数',
    )
    alive_case = fields.Integer(
        u'存活出院病例数',
    )
    cpr_failure = fields.Integer(
        u'CPR未成功病例数',
    )

    @api.multi
    def unlink(self):
        for emerg in self:
            emerg.mqc_id.unlink()
        return super(Emergency, self).unlink()

    # _sql_constraints = [
    #     ('year_month_uniq',
    #      'UNIQUE (year_month)',
    #      u'本月只能上报一次数据')
    # ]
