# -*- coding: utf-8 -*-
from odoo import http

# class HrPayrollEuropoles(http.Controller):
#     @http.route('/hr_payroll_europoles/hr_payroll_europoles/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_payroll_europoles/hr_payroll_europoles/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_payroll_europoles.listing', {
#             'root': '/hr_payroll_europoles/hr_payroll_europoles',
#             'objects': http.request.env['hr_payroll_europoles.hr_payroll_europoles'].search([]),
#         })

#     @http.route('/hr_payroll_europoles/hr_payroll_europoles/objects/<model("hr_payroll_europoles.hr_payroll_europoles"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_payroll_europoles.object', {
#             'object': obj
#         })