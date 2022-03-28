from odoo.exceptions import Warning
from odoo import models, fields, api, _

class Location(models.Model):

    _name = 'employee.location'
    _description = 'Employee Location'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name',required="1")
    company_id = fields.Many2one('res.company',default=lambda self: self.env.user.company_id,string='Company',readonly=False,)