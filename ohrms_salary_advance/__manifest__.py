# -*- coding: utf-8 -*-

{
    'name': 'Advance Salary',
    'version': '14.0.1.0.0',
    'summary': 'Advance Salary In HR',
    'description': """Helps you to manage Advance Salary Request of your company's staff.""",
    'category': 'Generic Modules/Human Resources',
    'author': 'Advanced Solutions && Cybrosys Techno solutions',
    'company': 'Advanced Solutions',
    'website': "https://www.advanced.qa",
    'depends': ['hr_payroll', 'hr', 'account', 'hr_contract',],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/salary_structure.xml',
        'views/salary_advance.xml',
    ],
    'images': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}

