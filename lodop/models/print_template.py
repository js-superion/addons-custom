from openerp import fields, models

class PrintTemplate(models.Model):
    _name = 'print.template'

    res_model = fields.Many2one('ir.model', string='Model', required=True)
    template = fields.Text('Template')
    active = fields.Boolean('Active')
    key = fields.Char('Key')
