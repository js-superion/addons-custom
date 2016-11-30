# -*- coding: utf-8 -*-
from openerp import http

# class Mqc(http.Controller):
#     @http.route('/mqc/mqc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mqc/mqc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mqc.listing', {
#             'root': '/mqc/mqc',
#             'objects': http.request.env['mqc.mqc'].search([]),
#         })

#     @http.route('/mqc/mqc/objects/<model("mqc.mqc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mqc.object', {
#             'object': obj
#         })