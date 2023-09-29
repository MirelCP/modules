# -*- coding: utf-8 -*-
{
    'name': "Library",

    'summary': """
        Module to manage a library""",

    'description': """
        Module to manage a library, in progress
    """,

    'author': "Mirel",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/library_book_view.xml',
        'views/library_author_view.xml',
        'views/res_users_view_extension.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
