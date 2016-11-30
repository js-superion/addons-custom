from openerp import http
from openerp import SUPERUSER_ID
from openerp.http import request


class PrintController(http.Controller):
    @http.route('/print/template/get', type='http', auth='public', method=['POST'], website=True)
    def print_template_get(self, **post):
        model = post.get('model', '')
        model_id = request.registry['ir.model'].search_read(request.cr, SUPERUSER_ID,
            domain=[('model', '=', model)],
            fields=['id'],
            limit=1,
        )
        if model_id:
            key = post.get('key', '')
            if key=='':
                dm = [('res_model', '=', model_id[0]['id']), ('active', '=', True)]
            else:
                dm = [('res_model', '=', model_id[0]['id']), ('active', '=', True), ('key', '=', key)]
            data = request.env['print.template'].search_read(
                domain=dm,
                fields=['template'],
                limit=1,
            )
            if data:
                return data[0]['template']
            else:
                rst=''
                columns = request.env[model]._columns
                for field in columns:
                    if columns[field]._type!='one2many':
                        rst+="LODOP.ADD_PRINT_TEXTA('"+field+"', 0, 0, 40, 20, '"+field+"');"
                return rst
        else:
            return ''

    @http.route('/print/get', type='http', auth='public', method=['POST'], website=True)
    def print_get(self, **post):
        model = post.get('model', '')
        model_id = request.registry['ir.model'].search_read(request.cr, SUPERUSER_ID,
            domain=[('model', '=', model)],
            fields=['id'],
            limit=1,
        )
        if model_id:
            key = post.get('key', '')
            if key == '':
                dm = [('res_model', '=', model_id[0]['id']), ('active', '=', True)]
            else:
                dm = [('res_model', '=', model_id[0]['id']), ('active', '=', True), ('key', '=', key)]
            data = request.env['print.template'].search_read(
                domain=dm,
                fields=['template'],
                limit=1,
            )
            if data:
                template = data[0]['template']
                ids = []
                idsStr = post.get('ids', '').split(',')
                pieces = post.get('pieces','1')
                for idStr in idsStr:
                    ids.append(int(idStr))
                objs = request.env[model].browse(ids)
                rst = ''
                for obj in objs:
                    tmp = template
                    tmp = tmp.replace(tmp.split('\r\n')[0], '')
                    for field in obj._fields:
                        if field in tmp:
                            if obj[field]:
                                if obj._fields[field].type == 'many2one':
                                    if obj[field]: tmp = tmp.replace(field, obj[field].name)
                                if obj._fields[field].type == 'integer':
                                    tmp = tmp.replace(field, str(obj[field]))
                                if obj._fields[field].type == 'datetime':
                                    tmp = tmp.replace(field, obj[field])
                                if obj._fields[field].type == 'char':
                                    tmp = tmp.replace(field, obj[field])
                                if obj._fields[field].type == 'text':
                                    tmp = tmp.replace(field, obj[field])
                            else:
                                tmp=tmp.replace(field,'')
                    for piece in range(int(pieces)):
                        if rst != '':
                            rst += "LODOP.NewPage();"
                        rst += tmp
                return rst
            else:
                return ''
        else:
            return ''

    @http.route('/print/count', type='http', auth='public', method=['POST'], website=True)
    def print_count(self, **post):
        model = post.get('model', '')
        ids = []
        idsStr = post.get('ids', '').split(',')
        for idStr in idsStr:
            ids.append(int(idStr))
        objs = request.env[model].browse(ids)

        for obj in objs:
            if obj._fields['print_times']:
                if obj.print_times:
                    obj.print_times += 1
                else:
                    obj.print_times = 1
                request.registry[model].write(request.cr, request.uid, obj.id, {'print_times': obj.print_times})

    @http.route('/print/template/set', type='http', auth='public', method=['POST'], website=True)
    def print_template_set(self, **post):
        model = post.get('model', '')
        model_id = request.registry['ir.model'].search_read(request.cr, SUPERUSER_ID,
            domain=[('model', '=', model)],
            fields=['id'],
            limit=1,
        )
        if model_id:
            key = post.get('key', '')
            template = post.get('template', '')

            data = request.env['print.template'].search_read(
                domain=[('res_model', '=', model_id[0]['id']), ('active', '=', True), ('key', '=', key)],
                fields=['id', 'template'],
                limit=1,
            )
            if data:
                request.registry['print.template'].write(request.cr, request.uid, data[0]['id'], {'res_model': model_id[0]['id'], 'template': template, 'active': True, 'key': key})
            else:
                request.env['print.template'].create({'res_model': model_id[0]['id'], 'template': template, 'active': True, 'key': key})
        return ''