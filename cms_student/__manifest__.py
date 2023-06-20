{
    'name': 'Student',
    'version': '16.0.1.0.0',
    'author': 'BSCS',
    'website': 'http://www.edu.pk',
    'category': 'Student Management System',
    'license': "AGPL-3",
    'Summary': 'A Module For Student Management System',
    'images': ['static/description/icon.jpg'],
    'depends': ['base', 'hr'],
    'data': ['security/cms_student_security.xml',
             'security/ir.model.access.csv',
             'views/cms_student_view.xml',
             'views/hr_employee_view.xml',
             'views/cms_student_menu.xml'],
            
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    #'post_init_hook': '_method_run_before_installation',
}

############# When to restart the Odoo Server  #############
# Restart the Odoo Server when changes are made in Python files
# Don't restart the Odoo server, when changes are made in XML files (View)

############# When to upgrade the Odoo modules #############
# Upgrade module when changes are made Schema level (Python class attribute, DB constrains)
# Upgrade module when changes are made in XML files (View)


