# -*- coding: utf-8 -*-
# from odoo import http


# class CustomDronena(http.Controller):
#     @http.route('/custom_dronena/custom_dronena', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_dronena/custom_dronena/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_dronena.listing', {
#             'root': '/custom_dronena/custom_dronena',
#             'objects': http.request.env['custom_dronena.custom_dronena'].search([]),
#         })

#     @http.route('/custom_dronena/custom_dronena/objects/<model("custom_dronena.custom_dronena"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_dronena.object', {
#             'object': obj
#         })
