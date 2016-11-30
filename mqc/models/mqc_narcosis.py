# -*- coding: utf-8 -*-
from openerp import models, fields,api

class Narcosis(models.Model):
    _name = "mqc.narcosis" #dialysis 透析
    _description = u"麻醉质控"
    _inherits = {'mqc.mqc': 'mqc_id'}
    mqc_id = fields.Many2one('mqc.mqc', u'报表id', required=True,
                              ondelete='cascade')
    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))
    _rec_name = 'year_month'

     #一、手术室内麻醉数（例次）
    # ASA分级手术病人麻醉数
    field1 = fields.Float(u'麻醉总数')
    field2 = fields.Float(u'Ⅰ级')
    field3 = fields.Float(u'Ⅱ级')
    field4 = fields.Float(u'Ⅰ-Ⅱ级所占比例%')
    field5 = fields.Float(u'Ⅲ级')
    field6 = fields.Float(u'Ⅳ级')
    field7 = fields.Float(u'Ⅴ级')
    field8 = fields.Float(u'Ⅲ-Ⅴ级所占比例%')
    field9 = fields.Float(u'急诊手术例数')
    field10 = fields.Float(u'急诊手术所占比例%')
    # 麻醉分类数
    field11 = fields.Float(u'全麻总数') #全身麻醉数
    field12 = fields.Float(u'吸入全麻')
    field13 = fields.Float(u'静脉全麻')
    field14 = fields.Float(u'静吸复合')
    field15 = fields.Float(u'联合麻醉')
    field16 = fields.Float(u'腰麻') #椎管内麻醉数
    field17 = fields.Float(u'腰硬联合')
    field18 = fields.Float(u'管内麻醉术硬膜外')
    field19 = fields.Float(u'MAC麻醉术')
    field20 = fields.Float(u'其他麻醉数')

    #专科麻醉数
    field21 = fields.Float(u'脑外科')
    field22 = fields.Float(u'胸外科')
    field23 = fields.Float(u'心血管外科')
    field24 = fields.Float(u'小儿外科')
    field25 = fields.Float(u'产科')
    #二、手术室外麻醉与镇痛数 - 手术室外麻醉与MAC数（例次）
    field26 = fields.Float(u'胃肠道') #有创或无创检查
    field27 = fields.Float(u'呼吸系统')
    field28 = fields.Float(u'其他')
    field29 = fields.Float(u'介入手术治疗')
    field30 = fields.Float(u'人流手术')
    field31 = fields.Float(u'分娩镇痛')
    field32 = fields.Float(u'其他')
    #三、收住、诊治病人数（例次）
    field33 = fields.Float(u'PACU') #收住病人
    field34 = fields.Float(u'AICU')
    field35 = fields.Float(u'疼痛病房')
    field36 = fields.Float(u'疼痛门诊')
    #四、麻醉成功率(例次 / %)
    field37 = fields.Float(u'成功例数')#神经(含神经丛)阻滞成功率
    field38 = fields.Float(u'同期总数')
    field39 = fields.Float(u'成功率%')
    field40 = fields.Float(u'成功例数')#硬膜外阻滞成功率
    field41 = fields.Float(u'同期总数')
    field42 = fields.Float(u'成功率%')
    field43 = fields.Float(u'成功例数')#困难气道处理成功率
    field44 = fields.Float(u'同期总数')
    field45 = fields.Float(u'成功率%')
    #五、麻醉死亡率、并发症发生率(例次/%)
    field46 = fields.Float(u'死亡例数') #麻醉相关死亡率
    field47 = fields.Float(u'同期麻醉总数')
    field48 = fields.Float(u'死亡率%')
    field49 = fields.Float(u'感染例数')#有创性麻醉操作感染发生率
    field50 = fields.Float(u'同期操作总数')
    field51 = fields.Float(u'感染率%')
    field52 = fields.Float(u'发生例数')#椎管内麻醉神经并发症发生率
    field53 = fields.Float(u'同期椎管内麻醉总数')
    field54 = fields.Float(u'发生率%')

    field55 = fields.Float(u'感染例数')#有创性监测操作感染发生率
    field56 = fields.Float(u'同期操作总数')
    field57 = fields.Float(u'感染率%')
    field58 = fields.Float(u'头痛例数')#腰麻后头痛发生率
    field59 = fields.Float(u'同期腰麻总数')
    field60 = fields.Float(u'发生率%')
    field61 = fields.Float(u'发生例数') #硬膜外麻醉硬脊膜穿破发生率
    field62 = fields.Float(u'同期硬膜外麻醉总数')
    field63 = fields.Float(u'发生率%')

    field64 = fields.Float(u'发生例数') #苏醒延迟发生率
    field65 = fields.Float(u'同期全麻总数')
    field66 = fields.Float(u'发生率%')
    field67 = fields.Float(u'发生例数') #全麻术中知晓发生率
    field68 = fields.Float(u'同期全麻例数')
    field69 = fields.Float(u'发生率%')
    field70 = fields.Float(u'发生例数') #硬膜外麻醉血管损伤发生率
    field71 = fields.Float(u'同期硬膜外麻醉总数')
    field72 = fields.Float(u'发生率%')

    field73 = fields.Float(u'发生例数') #麻醉期间心跳骤停发生率
    field74 = fields.Float(u'同期全麻总数')
    field75 = fields.Float(u'发生率%')
    field76 = fields.Float(u'回收例数') #自体血回收率
    field77 = fields.Float(u'同期全麻总数')
    field78 = fields.Float(u'回收率%')

    #六、术前评估与术后随访率(例次/%)
    field79 = fields.Float(u'麻醉前访视记录例数') #麻醉前访视记录
    field80 = fields.Float(u'同期麻醉总数')
    field81 = fields.Float(u'访视率%')
    field82 = fields.Float(u'麻醉后随访记录例数') #麻醉后访视记录
    field83 = fields.Float(u'同期麻醉总数')
    field84 = fields.Float(u'随访率%')
    field85 = fields.Float(u'镇痛例数') #术后镇痛率
    field86 = fields.Float(u'同期麻醉总数')
    field87 = fields.Float(u'镇痛率%')

    field88 = fields.Float(u'签同意书例数') #麻醉知情同意书
    field89 = fields.Float(u'同期麻醉总数')
    field90 = fields.Float(u'签订率%')

    #七、手术台及床位设置（台张）- 手术台及床位数
    field91 = fields.Float(u'手术台数(台)手术室内实际使用台数')
    field92 = fields.Float(u'手术台数(台)手术室外实际使用台数')
    field93 = fields.Float(u'床位数(张)麻醉后监护室(PACU)')
    field94 = fields.Float(u'床位数(张)麻醉科疼痛病房')

    #八、医师、护士与手术台比例
    field95 = fields.Float(u'临床麻醉医师总人数(不含ICU及疼痛医师)')
    field96 = fields.Float(u'手术台与医师总数比例')
    field97 = fields.Float(u'主治医师以上人员数')
    field98 = fields.Float(u'手术台与主治医师以上人员比例')
    field99 = fields.Float(u'临床麻醉护士总人数(不含ICU及疼痛护士)')
    field100 = fields.Float(u'手术台与护士比例')

    #九、收费统计（%）
    field101 = fields.Float(u'药品占医疗收入百分比')
    field102 = fields.Float(u'麻醉科总收入(亿)')
    field103 = fields.Float(u'医用材料占医疗收入百分比')
    field104 = fields.Float(u'医院总收入（亿）')
    field105 = fields.Float(u'AICU抗生素占药品费用比')
    field106 = fields.Float(u'麻醉科总收入占医院总收入百分比（%）')

    # _sql_constraints = [
    #     ('year_month_uniq',
    #      'UNIQUE (year_month)',
    #      u'本月只能上报一次数据')
    # ]

    @api.multi
    def unlink(self):
        for item in self:
            item.mqc_id.unlink()
        return super(Narcosis, self).unlink()





