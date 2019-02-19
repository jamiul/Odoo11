# -*- coding: utf-8 -*-
from odoo import http

# class IqraInvoice(http.Controller):
#     @http.route('/iqra_invoice/iqra_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iqra_invoice/iqra_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iqra_invoice.listing', {
#             'root': '/iqra_invoice/iqra_invoice',
#             'objects': http.request.env['iqra_invoice.iqra_invoice'].search([]),
#         })

#     @http.route('/iqra_invoice/iqra_invoice/objects/<model("iqra_invoice.iqra_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iqra_invoice.object', {
#             'object': obj
#         })