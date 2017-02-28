# -*- coding: utf-8 -*-
{
    'name': "wenty",

    'summary': """
        简单演示版本
        """,

    'description': """
        解决文泰电商目前发货时，手动匹配片区的痛点
    """,

    'author': "江知晓",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'wenty',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/wenty_security.xml',
        'security/ir.model.access.csv',
        'views/wenty.xml',
        'views/templates.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application':True
}