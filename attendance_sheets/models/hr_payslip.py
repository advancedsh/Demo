# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime


class HRPayslip(models.Model):
    _inherit = 'hr.payslip'

    work = fields.Float(string="Work")
    work_over_time = fields.Float(string="Work Over Time")
    sick = fields.Float(string="Total Sick")
    official = fields.Float(string="Total Official")
    personal = fields.Float(string="Total Personal")
    salary_per_day = fields.Float(string="Salary Per Day")
    total_days = fields.Float(string="Total Days")
    overtime_friday = fields.Float(string="Overtime Friday")
    amount_overtime_friday = fields.Float(string="Amount Overtime Friday")
    overtime_ex_friday = fields.Float(string="Overtime Ex. Friday ")
    amount_overtime_ex_friday = fields.Float(string="Amount Overtime Ex. Friday")
    deduction = fields.Float(string="Deduction")

    def compute_sheet(self):
        res = super(HRPayslip, self).compute_sheet()
        for rec in self:
            attendance_obj = self.env['attendance.sheet'].search(
                [('employee_id', '=', rec.employee_id.id), ('date_from', '>=', rec.date_from),
                 ('date_to', '<=', rec.date_to)],limit=1)
            if attendance_obj:
                rec.work = attendance_obj.work
                rec.work_over_time = attendance_obj.work_over_time
                rec.sick = attendance_obj.sick
                rec.personal = attendance_obj.personal
                rec.salary_per_day = attendance_obj.salary_per_day
                rec.official = attendance_obj.official
                rec.overtime_friday = attendance_obj.overtime_friday
                rec.amount_overtime_friday = attendance_obj.amount_overtime_friday
                rec.overtime_ex_friday = attendance_obj.overtime_ex_friday
                rec.amount_overtime_ex_friday = attendance_obj.amount_overtime_ex_friday
                rec.deduction = attendance_obj.deduction
                rec.total_days = attendance_obj.total_days
        return res