# -*- coding: utf-8 -*-
from openerp import models, fields,api

class Drug(models.Model):
    _name = "mqc.drug" # 药事管理指标
    _description = u"药事管理指标"
    _inherits = {'mqc.mqc': 'mqc_id'}
    mqc_id = fields.Many2one('mqc.mqc', u'报表id', required=True,
                              ondelete='cascade')
    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))
    _rec_name = 'year_month'

    #1、一 般信息：
    lcypjqsl = fields.Integer(u'临床药品紧缺数量')
    ypcg_rate = fields.Integer(u'药品采供率(%)')
    yplgfh_rate = fields.Float(u'一品两规符合率(%)')
    ygcgdf = fields.Float(u'阳光采购得分')
    ysqmyyflyfhl = fields.Integer(u'医师签名与药房留样符合率(%)')
    ypsytyml = fields.Float(u'药品使用通用名率(%)')
    mzcffhl = fields.Float(u'门诊处方复核率(%)')
    ptcftphgl = fields.Integer(u'普通处方调配合格率(%)')
    tpypcmccl = fields.Float(u'调配药品的出门差错率(%)')
    zyyppfzlwc = fields.Float(u'中药饮片配方总量误差率(%)') #
    tpypyfylbsl = fields.Float(u'调配药品用法用量标识率(%)') #
    yjykpdwcl = fields.Integer(u'一级药库盘点误差率(%)')
    ejykpdwcl = fields.Float(u'二级药库盘点误差率(%)')
    wzglhgl = fields.Float(u'“五专”管理合格率(%)')
    szglhgl = fields.Float(u'"四专"管理合格率(%)')
    mjypzwxfl = fields.Float(u'麻精药品帐物相符率(%)')
    mjypcftphgl = fields.Float(u'麻精药品处方调配合格率(%)')
    mjzcfdpcyl = fields.Float(u'门、急诊处方点评抽样率(%)')
    dpcybls = fields.Float(u'点评出院病历数')
    dpdcfhgl = fields.Float(u'点评的处方合格率(%)')
    tbblfys = fields.Float(u'填报不良反应数')
    yzypblfybgsl = fields.Float(u'严重药品不良反应报告数量')
    yzb = fields.Float(u'药占比')
    mcjzrjyf = fields.Float(u'每次就诊人均药费')
    jzsykjyw_ratio = fields.Float(u'就诊使用抗菌药物的百分率(%)')
    jzsyzsyw_ratio = fields.Float(u'就诊使用注射药物的百分率(%)')
    jzsyzyzsj_ratio = fields.Float(u'就诊使用中药注射剂的百分率(%)')
    jzsygjjbyw_ratio = fields.Float(u'就诊使用国家基本药物的百分率(%)')
    dldlcyxgzs_case = fields.Float(u'独立的临床药学工作室数量')
    yxzyjsry_ratio = fields.Float(u'药学专业技术人员比例')

    # 专业信息（抗菌药物）
    zxkjywfjglhg_rate = fields.Float(u'执行抗菌药物分级管理合格率(%)')
    kjywpzpghg_rate = fields.Float(u'抗菌药物品种品规合格率(%)')
    kjywcfhg_rate = fields.Float(u'抗菌药物处方合格率(%)')
    zyhzkjywsyl = fields.Float(u'住院患者抗菌药物使用率(%)')
    zyhzkjywsyqd = fields.Float(u'住院患者抗菌药物使用强度')
    zyhzrjsykjywfy = fields.Float(u'住院患者人均使用抗菌药物费用')
    kjywfyzzyf_ratio = fields.Float(u'抗菌药物费用占总药费的百分率(%)')
    kjywcfbl = fields.Float(u'抗菌药物处方比例')
    kzkjywcfdpgz = fields.Float(u'开展抗菌药物处方点评工作')
    kzqjssyfykjywdpgz = fields.Float(u'开展清洁手术预防用抗菌药物点评工作')

    tssykjywylzkjywylbfb = fields.Float(u'"特殊使用"抗菌药物用量占抗菌药物用量的百分率(%)')
    jrsszdkjywyfsyl = fields.Float(u'介入手术诊断抗菌药物预防使用率(%)')
    qjsskjywyfsyl = fields.Float(u'清洁手术抗菌药物预防使用率(%)')
    qjssyfgyhgl = fields.Float(u'清洁手术预防给药合格率(%)（0.5 - 2h）')
    qjssyfgypzhgl = fields.Float(u'清洁手术预防给药品种合格率(%)')
    qjssyfgylchgl = fields.Float(u'清洁手术预防给药疗程合格率(%)')
    qjssyfgylhyyl = fields.Float(u'清洁手术预防给药联合用药率(%)')
    zyhzkjywbyxsjl = fields.Float(u'住院患者抗菌药物病原学送检率(%)')
    xzxsykjywbyxsjl = fields.Float(u'限制性使用抗菌药物病原学送检率(%)')
    tssykjywbyxsjl = fields.Float(u'特殊使用抗菌药物病原学送检率(%)')
    # 专业信息（临床药学）
    zzlcyssl = fields.Float(u'专职临床药师数量')
    cydkssl = fields.Float(u'参与的科室数量')
    cygldbzsl = fields.Float(u'参与管理的病种数量')
    kzbltlsl = fields.Float(u'开展病例讨论数量')
    kzyyjysl = fields.Float(u'开展用药教育数量')
    kzywzxsl = fields.Float(u'开展药物咨询数量')
    kzcfdpsl = fields.Float(u'开展处方点评数量')
    kzyzdpsl = fields.Float(u'开展医嘱点评数量')
    cylchzsl = fields.Float(u'参与临床会诊数量')
    kccfdpsl = fields.Float(u'开展处方点评数量')

    sxylsl = fields.Float(u'书写药历数量')
    sxynblyjfxsl = fields.Float(u'书写疑难病历以及分析数量')
    sxyyjysl = fields.Float(u'书写用药教育数量')
    jjyyzdsl = fields.Float(u'进行用药指导数量')
    jxzlywjc = fields.Float(u'进行治疗药物监测')
    tdm_pzsl = fields.Float(u'TDM品种数量')
    lcysgzsj = fields.Float(u'临床药师工作时间')
    kzrccfgz = fields.Float(u'开展日常查房工作')
    kzkjywlcsygl = fields.Float(u'开展抗菌药物临床使用管理')

    # _sql_constraints = [
    #     ('year_month_uniq',
    #      'UNIQUE (year_month)',
    #      u'本月只能上报一次数据')
    # ]
    @api.multi
    def unlink(self):
        for drug in self:
            drug.mqc_id.unlink()
        return super(Drug, self).unlink()

