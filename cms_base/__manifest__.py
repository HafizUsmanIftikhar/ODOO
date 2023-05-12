{
    'name': 'University',
    'version': '16.0.1.0.0',
    'sequence':-100,
    'author': 'BSCS',
    'website': 'http://www.edu.pk',
    'category': 'University Management System',
    'license': "AGPL-3",
    'Summary': 'A Module For university Management System',
    'images': ['static/description/icon.jpg'],
    'depends': [],
    'data': [
        'security/cms_base_security.xml',
        'views/cms_base.xml',
        'security/ir.model.access.csv',
        'views/cms_base_menu.xml',
    ],

    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    #'post_init_hook': '_method_run_before_installation',
}
