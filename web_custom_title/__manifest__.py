# -*- coding: utf-8 -*-
{
    'name': "Web Custom Title",
    'summary': "This module supports user to customize web window title in odoo.",
    'version': '1.1.0',
    'category': 'Extra Tools',
    'author': "phatdm <phatminh.0794@gmail.com>",
    'license': 'LGPL-3',
    'depends': ['base_setup'],
    'data': [
        # VIEWS
        'views/res_config.xml',
        'views/webclient_templates.xml',
    ],
    'demo': ['data/web_custom_title_demo.xml'],
    'images': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
