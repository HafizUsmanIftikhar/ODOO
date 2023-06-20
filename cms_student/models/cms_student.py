# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError

class CMSDepartment(models.Model):

    _name = 'cms.department'                # Internal name of a model
    _description = 'Department Information' # Description, displayed in Odoo user interface
    
    # Creating Hierarchy
    #_parent_store = True
    #_parent_name = "parent_id" # optional if field is 'parent_id'
    
    name = fields.Char('Name', required=True)
    parent_id = fields.Many2one('cms.department', string='Main Department', ondelete='restrict', index=True)    
    #sub_ids = fields.One2many('cms.department', 'parent_id', string='Sub Departments')
    #parent_path = fields.Char(string='Parent Path', compute='_compute_parent_path', store=True)

    @api.depends('parent_id.parent_path')
    def _compute_parent_path(self):
        for record in self:
            if record.parent_id:
                record.parent_path = '%s/%s' % (record.parent_id.parent_path, record.parent_id.name)
            else:
                record.parent_path = record.name

class CMSCourse(models.Model):

    _name = 'cms.course'                    
    _description = 'Course Information' 
        
    name = fields.Char('Name', required=True)
    course_offered_ids = fields.One2many('cms.course.offered', 'course_id', string='Course Offered')

class CMSCourseOffered(models.Model):

    _name = 'cms.course.offered'                    
    _description = 'Course Offered Information' 
        
    name = fields.Char('Name', required=True)
    from_date = fields.Datetime('From', default=date.today())
    end_date = fields.Datetime('To', default=date.today())
    course_id = fields.Many2one('cms.course', 'Course')
    student_ids = fields.Many2many('cms.student', 'cms_student_course_rel', 'course_id', 'student_id', string='Students')

class CMSStudent(models.Model):

    _name = 'cms.student'                # Internal name of a model
    _description = 'Student Information' # Description, displayed in Odoo user interface
        
    name = fields.Char('Student Name', required=True)
    father_name = fields.Char('Father Name', required=True)
    admission_no = fields.Char(string='Admission No.', readonly=True)
    registration_no = fields.Char(string='Registration No.', required=True) # string displayed in the Odoo user interface
    admission_date = fields.Datetime('Admission Date', default=date.today())
    birth_date = fields.Date('Date of Birth')
    cnic = fields.Char(string='CNIC')
    phone = fields.Char('Phone no.')
    email = fields.Char('Email')
    cgpa = fields.Float('CGPA', digits=(15,3))
    #cgpa = fields.Float('CGPA', digits='Custom') #First create record in Settings->Technical->Decimal Accuracy
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], 'Gender', required=True)
    state = fields.Selection([('draft', 'Draft'), ('verified', 'Verified'), ('approved', 'Approved'), 
                              ('cancelled', 'Cancelled')], 'Status', readonly=True, default="draft", help='Help here')
    active = fields.Boolean(default=True, help='Help here')
    #image = fields.Binary('image', widget="image")
    image = fields.Binary('Image', widget="image", options={'size': (500, 500)})
    department_id = fields.Many2one('cms.department', 'Department')
    approved_by = fields.Many2one('res.users', 'Approved By', readonly=True)
    course_ids = fields.Many2many('cms.course', 'cms_student_course_rel', 'student_id', 'course_id', string='Courses')
    remark = fields.Text('Remark')
    age = fields.Integer(compute='_compute_student_age', string='Age (Years)', readonly=True)
    
    _sql_constraints = [
        ('admisson_unique', 'UNIQUE(admission_no)',
        'Student Admission No. should be Unique.'),
        ('email_check', "CHECK(position('@' in email) > 0)", 
        "Email address must contain '@' symbol")]
    
    
    @api.constrains('cnic')
    def _check_cnic_formate(self):
        for rec in self:
            if rec.cnic:
                cnic = str(rec.cnic).strip().replace("-", "")
                if cnic:
                    if len(cnic) != 13:
                        raise ValidationError(_('''Student CNIC should be 13 digits!'''))
                    if not cnic.isdecimal():
                        raise ValidationError(_('''Student CNIC should have valid characters!'''))

    @api.depends('birth_date') 
    def _compute_student_age(self):
        '''Method to calculate student age'''
        for rec in self:
            rec.age = 0
            if rec.birth_date:
                today = date.today()
                years = today.year - rec.birth_date.year - ((today.month, today.day) < (rec.birth_date.month, rec.birth_date.day))
                rec.age = years
                

    def set_to_draft(self):
        '''Method to change state to draft'''
        self.state = 'draft'

    def set_to_verified(self):
        '''Method to change state to verified'''
        self.state = 'verified'

    def set_to_approved(self):
        '''Method to change state to approved'''
        
        if self.admission_date:        
            year = self.admission_date.year
            
            #self.admission_no  = str(year) + "-" + self.env['ir.sequence'].next_by_code('cms.student.code')  
        else:
            raise ValidationError(_('Please enter admission date for student %s)', self.name))

        self.state = 'approved'
        self.approved_by = self.env.uid

    def set_to_cancelled(self):
        '''Set the state to cancelled'''
        self.state = 'cancelled'

    #country_id = fields.Many2one('res.country', 'Country', ondelete='cascade') # 'cascasde', 'restrict', 'set null'
    #country_id = fields.Many2one(string="Country", comodel_name='res.country', help="Country") # keyword arguments
    
    #employees_ids = fields.One2many('hr.employee', 'department_id', string='Employee')

    #user_ids = fields.Many2many('res.user', 'res_user_group_rel', 'user_id', 'group_id', string='Users')
    #user_ids = fields.Many2many('res.user', string='Users', help='Help here')
    #Be careful using Relational Table: Database Table identifiers in PostgreSQL limit of 63 characters

    #_log_access = False
    #_rec_name = 'father_name'
    #_rec_names_search = ['name', 'code']
    #_order = "admission_date desc, name desc"

    #['|', ('active', '=', True), ('active', '=', False)]