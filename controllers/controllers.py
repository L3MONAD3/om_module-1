# -*- coding: utf-8 -*-
# from odoo import http


# class Module-1(http.Controller):
#     @http.route('/module-1/module-1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module-1/module-1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module-1.listing', {
#             'root': '/module-1/module-1',
#             'objects': http.request.env['module-1.module-1'].search([]),
#         })

#     @http.route('/module-1/module-1/objects/<model("module-1.module-1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module-1.object', {
#             'object': obj
#         })
