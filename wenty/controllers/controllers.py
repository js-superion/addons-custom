# -*- coding: utf-8 -*-
from odoo import http

# class Wentai(http.Controller):
#     @http.route('/wentai/wentai/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wentai/wentai/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wentai.listing', {
#             'root': '/wentai/wentai',
#             'objects': http.request.env['wentai.wentai'].search([]),
#         })

#     @http.route('/wentai/wentai/objects/<model("wentai.wentai"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wentai.object', {
#             'object': obj
#         })