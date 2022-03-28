from odoo.exceptions import Warning
from odoo import models, fields, api, _


class HrEmployeeContract(models.Model):
    _inherit = 'hr.contract'

    def _get_default_notice_days(self):
        if self.env['ir.config_parameter'].get_param(
                'hr_resignation.notice_period'):
            return self.env['ir.config_parameter'].get_param(
                            'hr_resignation.no_of_days')
        else:
            return 0

    notice_days = fields.Integer(string="Notice Period", default=_get_default_notice_days)

    location = fields.Many2one('employee.location', string="Location",related="employee_id.location" )

    # Allownace
    food_allownace = fields.Float(string='Food Allowance', store=True,)
    other_allownace = fields.Float(string='Other Allowance ', store=True)
    total_gross = fields.Float(string='Total', compute="get_total", store=True)

    @api.depends('wage', 'food_allownace','other_allownace')
    def get_total(self):
        for rec in self:
            rec.total_gross = rec.wage + rec.food_allownace + rec.other_allownace


