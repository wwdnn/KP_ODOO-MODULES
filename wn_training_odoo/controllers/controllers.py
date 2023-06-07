# -*- coding: utf-8 -*-
# from odoo import http


# class WnTrainingOdoo(http.Controller):
#     @http.route('/wn_training_odoo/wn_training_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wn_training_odoo/wn_training_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wn_training_odoo.listing', {
#             'root': '/wn_training_odoo/wn_training_odoo',
#             'objects': http.request.env['wn_training_odoo.wn_training_odoo'].search([]),
#         })

#     @http.route('/wn_training_odoo/wn_training_odoo/objects/<model("wn_training_odoo.wn_training_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wn_training_odoo.object', {
#             'object': obj
#         })
