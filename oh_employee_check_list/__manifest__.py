# -*- coding: utf-8 -*-

{
    'name': 'Employee Checklist',
    'version': '14.0.1.0.1',
    'summary': """Manages Employee's Entry & Exit Process""",
    'description': """This module is used to remembering the employee's entry and exit progress.""",
    'category': 'Human Resources',
    'author': 'Advanced Solutions && Cybrosys Techno solutions',
    'company': 'Advanced Solutions',
    'website': "https://www.advanced.qa",
    'depends': ['base', 'oh_employee_documents_expiry', 'mail', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/employee_form_inherit_view.xml',
        'views/checklist_view.xml',
        'views/employee_check_list_view.xml',
        'views/hr_plan_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}

