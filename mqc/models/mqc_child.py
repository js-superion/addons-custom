# -*- coding: utf-8 -*-
from openerp import api
from openerp import models, fields

class Child(models.Model):
    _name = "mqc.child" #child 儿科
    _description = u"儿科质控指标"
    _inherits = {'mqc.mqc': 'mqc_id'}
    mqc_id = fields.Many2one('mqc.mqc', u'报表id', required=True,
                              ondelete='cascade')
    _rec_name = 'year_month'
    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))

    #一般信息
    mzrs = fields.Float(u'门诊人数')
    jzrs = fields.Float(u'急诊人数')
    jzwzbqjs = fields.Float(u'急诊危重病抢救数')
    jztjrys = fields.Float(u'急诊途径入院数')
    myzzyrs = fields.Float(u'每月总住院人数')
    zybrlcljzls = fields.Float(u'住院病人临床路径种类数')
    lcljrjs = fields.Float(u'临床路径入径数')
    lcljrjl = fields.Float(u'临床路径入径率(%)')
    child_ids = fields.One2many('mqc.child.detail', 'child_id', u'病种信息',copy=True)

    @api.multi
    def unlink(self):
        for child in self:
            child.mqc_id.unlink()
        return super(Child, self).unlink()



#相关字典
class Disease(models.Model):
    _name = "mqc.disease"
    _description = u"病种字典"
    name = fields.Char(u'病种名',)



class ChildDetail(models.Model):
    _name = "mqc.child.detail"  # child 儿科
    _description = u"儿科质控明细"
    # 一般信息
    child_id = fields.Many2one('mqc.child', u'儿科主记录', required=True,)
    disease_name = fields.Many2one('mqc.disease',u'病种名称',required=True,)
    outp_case = fields.Float(u'门诊病人数')
    adm_case = fields.Float(u'住院病人数')
    zqgfyrs = fields.Float(u'支气管肺炎人数')
    zytfyrs = fields.Float(u'支原体肺炎人数')
    cure_rate = fields.Float(u'治愈好转率(%)')
    cbl = fields.Float(u'传报率(%)')
    out_hos_avg_days = fields.Float(u'出院者平均住院天数')
    out_hos_avg_cost = fields.Float(u'出院者平均住院费用')


