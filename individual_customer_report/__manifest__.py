# -*- coding: utf-8 -*-
{
    'name': "Individual Customer Invoice Report",

    'summary': """
        """,

    'description': """
        Individual customer report
    """,

    'author': "Xsellence Bangladesh Ltd.",
    'website': "https://xsellencebdltd.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        # 'views/assets.xml',
        'wizards/recap.xml',
        'reports/recap.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
}
