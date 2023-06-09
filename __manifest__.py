# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """
        Hospital Management System""",

    'description': """
        Hospital Management System
    """,

    'author': "Htoo Aung Khant",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hospital',
    'sequence': -100,
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['mail','product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'reports/report.xml',
        'reports/patient_card.xml',
    ],

    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    "application": True,
    "License": 'LGPL-3'
}