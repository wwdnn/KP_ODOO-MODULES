# -*- coding: utf-8 -*-
{
    
    'name': "Manajemen Transportasi (Wildan)",

    # ini versi singkat
    'summary': """
        Modul untuk Manajemen Transportasi""",

    # ini versi panjang
    'description': """
        Modul untuk Manajemen Transportasi dengan fitur: 
        - Kendaraan
        - Driver
        - Rute
        - Perjalanan
        - Penumpang
        - Tiket
        - Pembayaran
        - Laporan
    """,

    'author': "Wildan Setya Nugraha",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/action_server.xml',
        'data/sequence.xml',
        'data/data.xml',
        'views/menu_items.xml',
        'views/res_passenger_view.xml',
        'views/res_bus_view.xml',
        'views/bus_schedule_view.xml',
        'views/bus_route_view.xml',
        'views/hr_employee_view.xml',
        'report/report.xml',
        'report/report_bus_schedule.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
