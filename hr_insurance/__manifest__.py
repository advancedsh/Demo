# -*- coding: utf-8 -*-


{
    'name': 'Employee Insurance',
    'version': '14.0.1.0.0',
    'summary': """Employee Insurance Management for Open HRMS.""",
    'description': """Manages insurance amounts for employees to be deducted from salary""",
    'category': 'Human Resources',
    'author': 'Advanced Solutions && Cybrosys Techno solutions',
    'company': 'Advanced Solutions',
    'website': "https://www.advanced.qa",
    'depends': ['base', 'hr', 'hr_payroll', 'hr_employee_updation',],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_insurance_security.xml',
        'views/employee_insurance_view.xml',
        'views/insurance_salary_stucture.xml',
        'views/policy_management.xml',
              ],
    'images': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
