from collections import defaultdict
from datetime import datetime,date, time
import pytz
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class hr_payslip(models.Model):
    _inherit = 'hr.payslip'

    emp_code = fields.Char(string='EMP Code', related='employee_id.emp_code')
    department_id = fields.Many2one('hr.department', string="Department",related="employee_id.department_id",store=True)
    email = fields.Char(string='Email', related="employee_id.work_email",store=True)
    month_days = fields.Integer('Month Days', compute='_compute_month_days', store=True)


    # function to compute days of salary month
    @api.depends('date_from', 'date_to')
    def _compute_month_days(self):
        days = 0
        for rec in self:
            if rec.employee_id and rec.date_from and rec.date_to:
                days = ((rec.date_to - rec.date_from).days) + 1
            rec.month_days = days

    def compute_sheet(self):
        self.reflect_values()
        super(hr_payslip, self).compute_sheet()

    def reflect_values(self):
        for rec in self:
            if rec.employee_id and rec.date_from and rec.date_to:
                input_id = self.env['payroll.inputs'].search(
                    [('date_from', '=', rec.date_from), ('date_to', '=', rec.date_to),
                     ('employee_id', '=', rec.employee_id.id)], limit=1)
                if input_id:
                    rec.input_id = input_id.id
                    # fields
                    rec.working_days = input_id.working_days

                else:
                    rec.input_id = False
                    # Allowance
                    rec.working_days = 30


    input_id = fields.Many2one(comodel_name='payroll.inputs', string='Input Record')
    # Fields
    working_days = fields.Float(string='Working days')




