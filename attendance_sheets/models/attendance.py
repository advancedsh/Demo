# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime, timedelta
from odoo.exceptions import UserError
import calendar


class AttendanceSheet(models.Model):
    _name = 'attendance.sheet'
    _description = 'Attendance Sheet'
    _rec_name = 'employee_id'

    def _default_month(self):
        month = datetime.now().month
        self.month = str(month)
        return str(month)

    def get_employee_domain(self):
        if self.env.user.has_group('attendance_sheets.group_attendance_user') and not self.env.user.has_group(
                'attendance_sheets.group_attendance_manager'):
            emp_ids = self.env['hr.employee'].search(
                ['|', ('user_id', '=', self.env.user.id), ('parent_id.user_id', '=', self.env.user.id)]).ids
            result = [('id', 'in', emp_ids)]
        else:
            emp_ids = self.env['hr.employee'].search([]).ids
            result = [('id', 'in', emp_ids)]
        return result


    employee_code = fields.Char(string="Employee Code")
    employee_id = fields.Many2one(comodel_name='hr.employee', string="Employee Name", domain=get_employee_domain,
                                  required=True)
    month = fields.Selection(
        [('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'),
         ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'),
         ('10', 'October'), ('11', 'November'), ('12', 'December')], default=_default_month, string="Month")
    date_from = fields.Date(string="Date From", required=True)
    date_to = fields.Date(string="Date To", required=True)
    company_id = fields.Many2one('res.company', string="Company", required=True, readonly=True,
                                 default=lambda self: self.env.company)
    attendance_ids = fields.One2many('attendance.sheet.line', 'attendance_line_ids')

    work = fields.Float(string="Total Work", compute='compute_total_amount')
    work_over_time = fields.Float(string="Work Over Time", compute='compute_total_amount')
    sick = fields.Float(string="Total Sick", compute='compute_total_amount')
    official = fields.Float(string="Total Official", compute='compute_total_amount')
    personal = fields.Float(string="Total Personal", compute='compute_total_amount')
    salary_per_day = fields.Float(string="Salary Per Day", compute='compute_total_amount')
    total_days = fields.Float(string="Total Days", compute='compute_total_amount')
    overtime_friday = fields.Float(string="Overtime Friday", compute='compute_total_amount')
    amount_overtime_friday = fields.Float(string="Amount Overtime Friday", compute='compute_total_amount')
    overtime_ex_friday = fields.Float(string="Overtime Ex. Friday ", compute='compute_total_amount')
    amount_overtime_ex_friday = fields.Float(string="Amount Overtime Ex. Friday", compute='compute_total_amount')
    deduction = fields.Float(string="Deduction", compute='compute_total_amount')
    created_user_id = fields.Many2one('res.users', default=lambda self: self.env.user.id)

    @api.onchange('month')
    def onchange_month(self):
        for rec in self:
            if rec.month:
                month = rec.month
                year = date.today().year
                days = calendar.monthrange(year, int(month))
                rec.date_from = datetime(year, int(month), days[0])
                rec.date_to = datetime(year, int(month), days[1])

    @api.depends('attendance_ids')
    def compute_total_amount(self):
        work = len(self.attendance_ids.filtered(lambda x: x.att_type == 'w'))
        work_over_time = len(self.attendance_ids.filtered(lambda x: x.att_type == 'wo'))
        sick = len(self.attendance_ids.filtered(lambda x: x.att_type == 's'))
        official = len(self.attendance_ids.filtered(lambda x: x.att_type == 'o'))
        personal = len(self.attendance_ids.filtered(lambda x: x.att_type == 'p'))

        salary_per_day = self.employee_id.contract_id.wage / 30
        total_days = work + work_over_time - sick - personal

        overtime_friday = len(self.attendance_ids.filtered(lambda x: x.day == '7' and x.att_type == 'wo')) * 2
        amount_overtime_friday = overtime_friday * 5

        overtime_ex_friday = len(self.attendance_ids.filtered(lambda x: x.day != '7' and x.att_type == 'wo')) * 2
        amount_overtime_ex_friday = len(self.attendance_ids.filtered(lambda x: x.day == '7')) * 5

        deduction = salary_per_day * personal

        self.work = work if work else 0
        self.work_over_time = work_over_time if work_over_time else 0
        self.sick = sick if sick else 0
        self.official = official if official else 0
        self.personal = personal if personal else 0
        self.salary_per_day = salary_per_day
        self.total_days = total_days
        self.overtime_friday = overtime_friday
        self.amount_overtime_friday = amount_overtime_friday
        self.overtime_ex_friday = overtime_ex_friday
        self.amount_overtime_ex_friday = amount_overtime_ex_friday
        self.deduction = deduction


class AttendanceSheetLine(models.Model):
    _name = 'attendance.sheet.line'
    _description = 'Attendance Sheet Line'

    attendance_line_ids = fields.Many2one('attendance.sheet')
    att_date = fields.Date(string="Date")
    day = fields.Selection(
        [('1', 'Saturday'), ('2', 'Sunday'), ('3', 'Monday'), ('4', 'Tuesday'),
         ('5', 'Wednesday'), ('6', 'Thursday'), ('7', 'Friday')], string="Day")
    att_type = fields.Selection(
        [('w', 'W'), ('wo', 'WO'), ('s', 'S'), ('o', 'O'),
         ('p', 'P')], string="Type")
    oh = fields.Float(string="OH")

    @api.constrains('att_date')
    def constraint_act_date(self):
        """
        To restrict the entering of attendance not in date period
        :return:
        """
        for record in self:
            if record.att_date and record.attendance_line_ids.date_from and record.attendance_line_ids.date_to:
                if (fields.Date.from_string(record.att_date) < fields.Date.from_string(
                        record.attendance_line_ids.date_from)) or \
                        (fields.Date.from_string(record.att_date) > fields.Date.from_string(
                            record.attendance_line_ids.date_to)):
                    raise UserError("Date Mismatch. You can only add attendance between %s and %s"
                                    % (record.attendance_line_ids.date_from, record.attendance_line_ids.date_to))
