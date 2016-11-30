# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError
class Mouth(models.Model):
    _name = "mqc.mouth"
    _description = u'口腔质控'

    _inherits = {'mqc.mqc': 'mqc_id'}
    mqc_id = fields.Many2one('mqc.mqc', u'报表id', required=True,
                              ondelete='cascade')
    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))
    _rec_name = 'year_month'

    units_name = fields.Char( u'单位名称',)
    units_code = fields.Char(u'单位编码', )

    #一般信息
    outp_case = fields.Integer(  u'门诊病人数',)
    mr_acpt_rate = fields.Float(u'门诊病历书写合格率(%)',)
    presc_acpt_rate = fields.Float(u'处方合格率(%)',)
    device_wash_rate = fields.Float( u'口腔诊疗器械消毒或灭菌合格率(%)',)
    outp_presc_rate = fields.Float( u'门诊患者抗菌药物处方比例',)
    in_out_accord_diag = fields.Float(  u'入出院诊断符合率(%)',)
    accord_diag = fields.Float( u'手术前后诊断符合率(%)',)
    opr_cut_cure_rate= fields.Float(u'无菌手术切口甲级愈合率(%)',)
    inp_case= fields.Integer(u'出院病人数',)
    report_disease = fields.Many2one('mqc.mouth.special.disease',u'专科病种')
    report_tumor = fields.Many2one('mqc.mouth.parotid.tumor',u'腮腺肿瘤')


class MouthSpecial(models.Model):
    _name = "mqc.mouth.special.disease"
    _description = u'专科病种信息'

    _rec_name = 'year_month'
    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))
    # 专科病种信息
    rcc_acpt_rate = fields.Integer(u'根管治疗合格率(%)', )  # root canal recurrence
    use_blood_case = fields.Integer(u'乳牙根管治疗合格率(%)', )
    yzy_case = fields.Integer(u'牙周炎治疗例数', )
    yzygmpz_case = fields.Integer(u'牙周炎根面平整例数', )
    yyyzl_case = fields.Integer(u'牙龈炎治疗例数', )
    yyyzlhz_case = fields.Char(u'牙龈炎治疗好转例数', )
    kqbptxzl_case = fields.Integer(u'口腔扁平苔藓治疗例数', )
    shfjhzcss_case = fields.Char(u'术后非计划再次手术例数', )
    byhcx_rate = fields.Integer(u'拔牙后出血率(%)', )
    baygc_rate = fields.Char(u'拔牙后干槽率(%)', )
    ycfg_rate = fields.Integer(u'义齿返工率(%)', )
    ycjyyb_case = fields.Char(u'义齿基牙预备数', )
    ycjyybhg_case = fields.Integer(u'义齿基牙预备合格数', )
    zqzljjysjfh_rate = fields.Char(u'正畸治疗计划与实际完成符合率(%)', )
    zqylwjwz_rate = fields.Integer(u'正畸医疗文件的完整率(%)', )
    ypjj_rate = fields.Integer(u'牙片甲级率(%)', )
    blzdylczdfh_rate = fields.Integer(u'病理诊断与临床诊断符合率(%)', )
    zyhzkjywsy_rate = fields.Float(u'住院患者抗菌药物使用率(%)', )

class MouthTumor(models.Model):
    _name = "mqc.mouth.parotid.tumor"
    _description = u'腮腺肿瘤'

    _rec_name = 'year_month'
    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))
    cybr_case = fields.Float(u'出院病人数', )
    xzlqqcs_rate = fields.Float(u'行肿瘤全切除术例数', )
    sqpjzyr = fields.Float(u'术前平均住院日', )
    in_out_accord_diag_case = fields.Float(u'入出院诊断符合数', )
    opr_accord_diag = fields.Float(u'手术前后诊断符合数', )
    cure_case = fields.Float(u'治愈好转人数', )
    opr_complication_case = fields.Float(u'术后并发症发生数', )
    inp_avg_charge = fields.Float(u'出院者平均医疗费用', )
    drug_ratio = fields.Float(u'药品占总费用比例', )
    kyyw_drug_ratio = fields.Float(u'抗菌药物占药品费用比例', )
    avg_in_hos_days = fields.Float(u'平均住院天数', )

    @api.multi
    def unlink(self):
        for mouth in self:
            mouth.mqc_id.unlink()
        return super(Mouth, self).unlink()




