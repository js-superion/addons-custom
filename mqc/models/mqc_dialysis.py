# -*- coding: utf-8 -*-
from openerp import models, fields,api

class Dialysis(models.Model):
    _name = "mqc.dialysis" #dialysis 透析
    _description = u"肾病学质控"
    _inherits = {'mqc.mqc': 'mqc_id'}
    mqc_id = fields.Many2one('mqc.mqc', u'报表id', required=True,
                              ondelete='cascade')
    _rec_name = 'year_month'
    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))
    dept_doc_num = fields.Integer(u'肾内科专科医师人数')
    dept_nur_num = fields.Integer(u'专科护士人数')

    #肾小球疾病（非CKD5期）
    out_case = fields.Integer(u'出院病人数')
    avg_charge = fields.Float(u'出院者平均医疗费用')
    avg_days = fields.Integer(u'出院者平均住院日')
    accord_diag_case = fields.Integer(u'入出院诊断符合数')
    kidney_exam_case = fields.Integer(u'肾活检患者数')
    exam_complications = fields.Integer(u'肾活检术后并发症例数')
    pressure_control_case = fields.Integer(u'目标血压控制例数')
    iga_rate = fields.Float(u'初治IgA肾病患者进入肾活检临床路径百分率(%)')
    ln_rate = fields.Float(u'初治狼疮性肾炎进入肾活检临床路径百分率(%)') #狼疮性肾炎lupus nephritis

    #急性肾衰竭
    out_case1 = fields.Integer(u'出院病人数')
    cured_case = fields.Integer(u'治愈好转例数')
    avg_charge1 = fields.Float(u'出院者平均医疗费用')
    avg_days1 = fields.Integer(u'出院者平均住院日')
    kidney_exam_case1 = fields.Integer(u'肾活检患者数')
    exam_complications1 = fields.Integer(u'肾活检术后并发症例数')
    finish_cp_case = fields.Integer(u'开展完成临床路径例数')#cp clinic pathway
    acpt_dialysis_case = fields.Float(u'接受血液净化治疗患者百分率(%)')

    #慢性肾衰竭CKD5期
    out_case2 = fields.Integer(u'出院病人数')
    avg_charge2 = fields.Float(u'出院者平均医疗费用')
    avg_days2 = fields.Integer(u'出院者平均住院日')
    acpt_pd_case = fields.Integer(u'接受腹透管置入术患者数')
    acpt_iaf_case = fields.Integer(u'接受动静脉内瘘成形术患者数')#Internal arteriovenous fistula
    acpt_dvt_case = fields.Integer(u'接受血透长期深静脉导管置入患者数')#cp acpt accept缩写 dvt 深静脉置入


    #非住院维持性血液透析 mohc Minister of Health of the People's Republic of China  中国卫生部
    hd_num = fields.Integer(u'HD台数', )
    hdf_num = fields.Integer(u'HDF台', )
    crrt_num = fields.Integer(u'CRRT台', )
    dialysis_doc_num= fields.Integer(u'血液净化专职医生总数', )
    dialysis_nurse_num= fields.Integer(u'血液净化护士总数', )
    dialysis_pat_num = fields.Integer(u'长期血透患者数', )
    new_pat_num = fields.Integer(u'新增患者数', )
    dead_pat = fields.Integer(u'死亡患者数', )
    total_case = fields.Integer(u'血透总例次', )
    mohc_newpats= fields.Integer(u'新报患者数', )
    mohc_uppats = fields.Integer(u'更新患者数', )
    mohc_val_rate = fields.Float(u'填报合格率(%)', ) #validate rate
    dialyzer_reuse_rate = fields.Float(u'透析器复用患者百分率(%)', )
    week_excess12h_rate = fields.Float(u'血透时间>12h/周患者百分率(%)', )

    weight_val_rate = fields.Float(u'千体重达标率(%)', )
    weight_excess3kg_rate = fields.Integer(u'透析间期体重增加>3公斤患者数', )

    #非住院长期腹膜透析 #pd 缩写 Peritoneal dialysis
    create_type = fields.Selection([('1', u'是'), ('0', u'否')],
                                   u'是否开展腹膜透析')

    long_pd_case = fields.Integer(u'长期腹膜透析患者数', )
    pd_newpats = fields.Integer(u'新增患者数', )
    pd_cured_case = fields.Integer(u'退出患者数（不含死亡）', )
    pd_death_case = fields.Integer(u'死亡患者数', )
    pd_mohc_newpats = fields.Integer(u'新报患者数', )
    pd_mohc_uppats = fields.Integer(u'更新患者数', )
    pd_mohc_rate = fields.Float(u'填报合格率(%)', )
    peritonitis_case = fields.Integer(u'腹透相关腹膜炎发生例数', ) #peritonitis 腹膜炎

    @api.multi
    def unlink(self):
        for dialysis in self:
            dialysis.mqc_id.unlink()
        return super(Dialysis, self).unlink()


    # _sql_constraints = [
    #     ('year_month_uniq',
    #      'UNIQUE (year_month)',
    #      u'本月只能上报一次数据')
    # ]

