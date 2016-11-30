# -*- coding: utf-8 -*-

from openerp import models, fields,api
import datetime, pytz
from openerp.exceptions import ValidationError
class Pathology(models.Model):
    _name = "mqc.pathology"
    _description = u'病理质控指标'
    _inherits = {'mqc.mqc': 'mqc_id'}
    mqc_id = fields.Many2one('mqc.mqc', u'报表id', required=True,
                              ondelete='cascade')
    _rec_name = 'year_month'
    # def current_year_month(self):
    #     value = self.env['utils'].get_zero_time()
    #     value = value.strftime('%Y-%m')
    #     return value

    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))
    #专业信息
    frozen_section_case = fields.Integer(u'冰冻切片例数', )
    elivision_case = fields.Integer(u'免疫组化例数', )
    fish_case = fields.Integer(u'FISH检测例数', )
    details = fields.One2many('mqc.pathology.detail', 'pathology_id', u'护理质控明细',copy=True)

    @api.multi
    def unlink(self):
        for item in self:
            item.mqc_id.unlink()
        return super(Pathology, self).unlink()


    @api.constrains('year_month')
    def _check_year_month(self):
        domain = [
            ('create_uid', '=', self.create_uid.id),
            ('year_month', '=', self.year_month),
        ]
        length = len(self.search(domain))
        if length > 1:
            raise ValidationError(u'本月只能上报一次数据')






class PathologyExamType(models.Model):
    _name = 'mqc.pathology.examtype'
    _description = u'病理检查类型'
    name = fields.Char(u'检查类型')

class PathologyDetail(models.Model):
    _name = 'mqc.pathology.detail'
    _description = u'病理质控明细'
    pathology_id = fields.Many2one('mqc.pathology',u'病理主记录', required=True,)
    exam_type_id = fields.Many2one('mqc.pathology.examtype',u'病理检查类型')

    #诊断部分
    outp_exam_case = fields.Integer(u'门诊检查人数', )
    adm_exam_case = fields.Integer(u'住院检查人数', )
    rpt_less5d_reach = fields.Integer(u'常规报告≦5个工作日完成率(%)', )
    cellrpt_less2d_reach = fields.Integer(u'细胞学报告≦2个工作日完成率(%)', )
    path_diag_accuracy_rate = fields.Integer(u'病理诊断的准确率(%)', )
    cryostat_section_diag_rate = fields.Integer(u'冷冻切片与常规诊断的符合率(%)', )
    cryostat_section_less30min_rate = fields.Integer(u'冷冻切片≦30min完成例数', )
    is_review = fields.Boolean(u'执行复验制度（有/无）', )
    med_error_case = fields.Integer(u'医疗差错或过失发生次数', )
    #
    section_total = fields.Integer(u'切片总数', )
    grade_a_rate = fields.Float(u'甲级片率(%)', )
    grade_b_rate = fields.Float(u'乙级片率(%)', )
    grade_c_rate = fields.Float(u'丙级片率(%)', )
