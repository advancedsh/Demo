# -*- coding: utf-8 -*-

{
    'name': 'Loan Accounting',
    'version': '14.0.1.0.0',
    'summary': 'Open HRMS Loan Accounting',
    'description': """Create accounting entries for loan requests.""",
    'category': 'Human Resources',
    'author': 'Advanced Solutions && Cybrosys Techno solutions',
    'company': 'Advanced Solutions',
    'website': "https://www.advanced.qa",
    'depends': ['base', 'hr_payroll', 'hr', 'account', 'ohrms_loan',],
    'data': [
        'views/hr_loan_config.xml',
        'views/hr_loan_acc.xml',
    ],
    'images': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
