# -*- coding: utf-8 -*-
{
    'name': "HR Payroll Custom",
    'summary': """HR Payroll Custom """,
    'description': """HR Payroll Custom""",
    'author': "Advanced Solutions Co ltd.",
    'website': "http://www.advanced.qa",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Payroll',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr_contract','hr_employee_updation','hr_payroll'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/payroll_inputs.xml',
        'views/hr_payslip.xml',
        'data/mail_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}