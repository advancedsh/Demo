# -*- coding: utf-8 -*-

{
    'name': 'Loan Management',
    'version': '14.0.1.0.0',
    'summary': 'Manage Loan Requests',
    'description': """
        Helps you to manage Loan Requests of your company's staff.
        """,
    'category': 'Human Resources',
    'author': 'Advanced Solutions && Cybrosys Techno solutions',
    'company': 'Advanced Solutions',
    'website': "https://www.advanced.qa",
    'depends': ['base', 'hr_payroll', 'hr', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/hr_loan_seq.xml',
        'data/salary_rule_loan.xml',
        'views/hr_loan.xml',
        'views/hr_payroll.xml',
    ],
    'images': [''],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
