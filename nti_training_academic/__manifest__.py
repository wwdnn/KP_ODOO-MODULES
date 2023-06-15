# -*- coding: utf-8 -*-
{
    'name': "University",

    'summary': """
        Module for managing student's in a university""",

    'description': """
        Module for managing student's in a university 
        - Student
        - Course
        - Lecturer
        - Start Hour
        - End Hour
    """,

    'author': "Neural Technologies Indonesia",
    'website': "http://www.nti.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu_items.xml',
        'views/res_partner_view.xml',
        'views/subject_view.xml',
        'views/class_view.xml',
        'report/report.xml',
        'report/report_class.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
