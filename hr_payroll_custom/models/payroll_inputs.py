# -*- coding: utf-8 -*-

from collections import defaultdict
from datetime import datetime,date, time
import pytz
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class hr_payroll_inputs(models.Model):
    _name = 'payroll.inputs'
    _rec_name = 'employee_id'
    
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee')
    emp_code = fields.Char(string='Employee Code')
    date_from = fields.Date(string='From')
    date_to = fields.Date(string='To')

    # Fields
    working_days = fields.Float(string='Working days')


    @api.model
    def create(self, vals):
        if vals.get('emp_code'):
            employee = self.env['hr.employee'].search([('emp_code','=',vals.get('emp_code'))])
            if employee:
                vals['employee_id'] = employee.id
        return super(hr_payroll_inputs, self).create(vals)


