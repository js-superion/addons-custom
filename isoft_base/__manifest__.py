# -*- coding: utf-8 -*-
{
    'name': "isoft_base",

    'summary': """
        基础扩展库，包含工具类，程序框架，背景图片，样式，js等
        涉及到的公用资源，包，需要扩展的内容""",

    'description': """
        基础扩展库，包含工具类，程序框架，背景图片，样式，js等
    """,

    'author': "jzx",
    'website': "http://www.superion.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'isoft_base',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web','base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'data/ir_config_parameter.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],

    'installable': True,
    'application': True,
    'auto_install': False,
}