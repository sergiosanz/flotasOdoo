# -*- coding: utf-8 -*-
{
    'name': "flotas",

    'summary': """
        Examen final""",

    'description': """
        Me gustaria poder aprobar esto
    """,

    'author': "Sergio Sanz",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','baseModule'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}