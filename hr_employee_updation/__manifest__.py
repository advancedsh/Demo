# -*- coding: utf-8 -*-

{
    'name': 'Employee Info',
    'version': '14.0.1.0.0',
    'summary': """Adding Advanced Fields In Employee Master""",
    'description': 'This module helps you to add more information in employee records.',
    'category': 'Human Resources',
    'author': 'Advanced Solutions && Cybrosys Techno solutions',
    'company': 'Advanced Salutations',
    'website': "https://www.advanced.qa",
    'depends': ['base', 'hr', 'mail', 'hr_contract'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/location.xml',
        'views/contract_days_view.xml',
        'views/updation_config.xml',
        'views/hr_employee_view.xml',
        'views/hr_notification.xml',
    ],
    'images': [''],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
