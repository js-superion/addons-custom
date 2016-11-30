# -*- encoding: utf-8 -*-
##############################################################################
#
#    Samples module for Odoo Web Login Screen
#    Copyright (C) 2016- XUBI.ME (http://www.xubi.me)
#    @author binhnguyenxuan (https://www.linkedin.com/in/binh-nguyen-xuan-46556279)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
##############################################################################

import openerp
import openerp.modules.registry
import ast

from openerp.addons.web.controllers.main import Home

import datetime
import pytz

import openerp.http as http
from openerp.http import request
from openerp.addons.web.controllers.main import ExcelExport


# ----------------------------------------------------------
# OpenERP Web web Controllers
# ----------------------------------------------------------
class Home(Home):
    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        cr = request.cr
        uid = openerp.SUPERUSER_ID
        param_obj = request.registry.get('ir.config_parameter')
        request.params['disable_footer'] = ast.literal_eval(
            param_obj.get_param(cr, uid, 'login_form_disable_footer')) or False
        request.params['disable_database_manager'] = ast.literal_eval(
            param_obj.get_param(cr, uid, 'login_form_disable_database_manager')) or False

        change_background = ast.literal_eval(
            param_obj.get_param(cr, uid, 'login_form_change_background_by_hour')) or False
        if change_background:
            config_login_timezone = param_obj.get_param(cr, uid, 'login_form_change_background_timezone')
            tz = config_login_timezone and pytz.timezone(config_login_timezone) or pytz.utc
            current_hour = datetime.datetime.now(tz=tz).hour or 10

            if (current_hour >= 0 and current_hour < 3) or (current_hour >= 18 and current_hour < 24):  # Night
                request.params['background_src'] = param_obj.get_param(cr, uid, 'login_form_background_night') or ''
            elif current_hour >= 3 and current_hour < 7:  # Dawn
                request.params['background_src'] = param_obj.get_param(cr, uid, 'login_form_background_dawn') or ''
            elif current_hour >= 7 and current_hour < 16:  # Day
                request.params['background_src'] = param_obj.get_param(cr, uid, 'login_form_background_day') or ''
            else:  # Dusk
                request.params['background_src'] = param_obj.get_param(cr, uid, 'login_form_background_dusk') or ''
        else:
            request.params['background_src'] = param_obj.get_param(cr, uid, 'login_form_background_default') or ''
        return super(Home, self).web_login(redirect, **kw)


try:
    import json
except ImportError:
    import simplejson as json



class ExcelExportView(ExcelExport):
    def __getattribute__(self, name):
        if name == 'fmt':
            raise AttributeError()
        return super(ExcelExportView, self).__getattribute__(name)

    @http.route('/web/export/xls_view', type='http', auth='user')
    def export_xls_view(self, data, token):
        data = json.loads(data)
        model = data.get('model', [])
        columns_headers = data.get('headers', [])
        rows = data.get('rows', [])

        return request.make_response(
            self.from_data(columns_headers, rows),
            headers=[
                ('Content-Disposition', 'attachment; filename="%s"'
                 % self.filename(model)),
                ('Content-Type', self.content_type)
            ],
            cookies={'fileToken': token}
        )
