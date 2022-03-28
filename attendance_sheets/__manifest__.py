# -*- coding: utf-8 -*-
{
    'name': "Attendance Sheets",

    'summary': """This Module Helps to calculate attendance sheet based on attendance type""",
    'description': """This Module Helps to calculate attendance sheet based on attendance type""",
    'author': "Advanced Solutions",
    'website': "http://www.advanced.qa",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'HR',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','hr','hr_payroll'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/attendance.xml',
        'views/hr_payslip.xml',
    ],
    'application': True,
}
