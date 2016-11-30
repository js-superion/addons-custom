# -*- coding: utf-8 -*-
from openerp import http

# class CarShare(http.Controller):
#     @http.route('/car_share/car_share/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/car_share/car_share/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('car_share.listing', {
#             'root': '/car_share/car_share',
#             'objects': http.request.env['car_share.car_share'].search([]),
#         })

#     @http.route('/car_share/car_share/objects/<model("car_share.car_share"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('car_share.object', {
#             'object': obj
#         })