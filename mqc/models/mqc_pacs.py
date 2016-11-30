# -*- coding: utf-8 -*-

from openerp import models, fields,api

class Pacs(models.Model):
    _name = "mqc.pacs"
    _description = u'医学影像质控'
    _inherits = {'mqc.mqc': 'mqc_id'}
    mqc_id = fields.Many2one('mqc.mqc', u'报表id', required=True,
                             ondelete='cascade')
    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))
    _rec_name = 'year_month'
    #介入放射指标
    intervene_id = fields.Many2one('mqc.pacs.intervene', u'介入放射', required=True)
    details = fields.One2many('mqc.pacs.detail', 'pacs_id', u'影像质控明细',copy=True)

    @api.multi
    def unlink(self):
        for item in self:
            item.mqc_id.unlink()
        return super(Pacs, self).unlink()


    # _sql_constraints = [
    #     ('year_month_uniq',
    #      'UNIQUE (year_month)',
    #      u'本月只能上报一次数据')
    # ]

class PacsIntervene(models.Model):
    _name = 'mqc.pacs.intervene'
    _description = u'介入放射指标'
    # 诊断部分
    open_bed_case = fields.Integer(u'开放床位数', )
    inp_case = fields.Integer(u'入院病人数', )
    outp_case = fields.Integer(u'出院病人数', )
    bed_use_rate = fields.Float(u'床位使用率(%)', )
    in_out_accord_diag = fields.Integer(u'入出院诊断符合率(%)', )
    self_pay_case = fields.Integer(u'自费例数', )
    insurance_pats = fields.Integer(u'医保例数', )
    critical_pat_case = fields.Integer(u'危重病例数', )
    serial_rescue_case = fields.Integer(u'危重病例抢救成功数', )

    avg_adm_days = fields.Integer(u'平均住院日', )
    outp_avg_charge = fields.Integer(u'出院者平均医疗费用', )
    drug_ratio = fields.Integer(u'药品占总费用比例', )
    opr_complication_rate = fields.Integer(u'术后并发症发生率(%)', )
    antibiotics_prevent_rate = fields.Integer(u'预防抗生素使用率(%)', )
    inblood_cure_case = fields.Integer(u'血管内治疗人数', )
    unblood_cure_case = fields.Integer(u'非血管治疗人数', )
    internal_medicine_case = fields.Integer(u'内科治疗人数', )
    sjjr_case = fields.Integer(u'神经介入诊疗人数', )
    opr_complication_rate2 = fields.Float(u'术后并发症数/率(%)', )
    inhos_infect_rate = fields.Float(u'院内感染数/率(%)', )
    accord_diag_rate = fields.Float(u'临床与病理诊断符合数/率(%)', )
    outhos_cure_case = fields.Integer(u'出院治愈人数', )
    outhos_better_case = fields.Integer(u'出院好转人数', )
    outhos_uncure_case = fields.Integer(u'出院未愈人数', )
    outhos_death_case = fields.Integer(u'出院死亡人数', )
    outhos_other_case = fields.Integer(u'其他（例）', )
    outhos_better_rate = fields.Integer(u'出院好转率(%)', )
    #手术并发症
    hematoma_case = fields.Integer(u'血肿例数', ) #hematoma 血肿
    fa_case = fields.Integer(u'假性动脉瘤例数', ) #FA; false aneurysm
    vf_case = fields.Integer(u'静脉瘘例数', ) #venous fistula 静脉瘘
    vw_tear_case = fields.Integer(u'血管壁撕裂例数', ) #vascular wall
    opr_infect_case = fields.Integer(u'术后感染例数', )
    em_case = fields.Integer(u'异位栓塞例数', ) #Ectopic embolism






class PacsDevice(models.Model):
    _name = "mqc.pacs.device"
    _description = u"医学影像设备"
    name = fields.Char(u'设备名称', )


class PacsDetail(models.Model):
    _name = 'mqc.pacs.detail'
    _description = u'医学影像指标明细（CT,MRI,普放）'
    pacs_id = fields.Many2one('mqc.pacs',u'医学影像主记录', required=True,)
    device_id = fields.Many2one('mqc.pacs.device',u'影像设备')

    #诊断部分
    outp_exam_case = fields.Integer(u'门诊检查人数', )
    outp_total = fields.Integer(u'门诊总量', )
    inp_exam_case = fields.Integer(u'住院检查人数', )
    adm_exam_case = fields.Integer(u'住院总量', )
    inp_accord_diag = fields.Integer(u'入院诊断符合数', )
    outp_accord_diag = fields.Integer(u'出院诊断符合数', )
    cns_exam_case = fields.Integer(u'中枢神经系统检查人数', ) #central nervous system

    bone_exam_case = fields.Integer(u'骨骼/关节检查人数', )
    urinary_genital_case = fields.Integer(u'泌尿/生殖系统检查人数', ) #urinary泌尿，genital 生殖
    breath_exam_case = fields.Integer(u'呼吸系统检查人数', )

    digestive_case = fields.Integer(u'消化系统检查人数', ) #digestive 消化
    diag_error_case = fields.Integer(u'影像诊断误/漏诊数', )
    infect_report_case = fields.Integer(u'传染病报告人数', )
    critical_value_case = fields.Integer(u'危急值报告人数', )
    crc_case = fields.Integer(u'结直肠癌病例数', ) #colorectal cancer (CRC)
    contrast_agent_reaction = fields.Integer(u'对比剂不良反应', )
    positive_rate = fields.Integer(u'检查阳性率(%)', )
    finish_case = fields.Integer(u'功能成像完成人数', )
    enhance_rate = fields.Integer(u'增强率(%)', )
