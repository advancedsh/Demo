# -*- coding: utf-8 -*-


{
    'name': 'HR Organizational Chart',
    'version': '14.0.1.0.0',
    'summary': 'HR Employees organizational chart',
    'description': 'HR Employees organizational chart',
    'author': 'Advanced Solutions && Cybrosys Techno solutions',
    'company': 'Advanced Salutations',
    'website': "https://www.advanced.qa",
    'category': 'Human Resources',
    'website': "https://www.openhrms.com",
    'depends': ['hr'],
    'data': [
        'views/show_employee_chart.xml',
        'views/assets.xml',
    ],
    'qweb': ['static/src/xml/chart_view.xml'],
    'images': [''],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}