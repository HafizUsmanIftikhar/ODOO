from odoo import models, fields, api, _


class CMSDepartment(models.Model):
    _name = 'cms.department'
    _description = 'Department Information'

    name = fields.Char('Name', required=True)
    programs_offered_ids = fields.One2many('cms.program', 'department_id', string='Programs')


class CMSProgram(models.Model):
    _name = 'cms.program'
    _description = 'Program Offered Information'

    name = fields.Char('Name', required=True)
    duration = fields.Char('duration', required=True)
    eligibility = fields.Char('eligibility', required=True)

    department_id = fields.Many2one('cms.department', 'Programs')

    program_line_ids = fields.One2many('cms.program.line', 'program_id', string='Program line')
    programoffered_ids = fields.One2many('cms.program.offered', 'program_id', string='Program Offered')


class CMSProgramLine(models.Model):
    _name = 'cms.program.line'
    _description = 'Program Offered Information'

    name = fields.Char('Name', required=True)
    semester = fields.Char('semester', required=True)
    course = fields.Char('course', required=True)

    program_id = fields.Many2one('cms.program', 'program')
    course_ids = fields.One2many('cms.course', 'program_line_id', string='Courses')


class CMSProgramOffered(models.Model):
    _name = 'cms.program.offered'
    _description = 'Program Offered Information'

    course_code = fields.Char('course_code', required=True)
    name = fields.Char('Name', required=True)
    credits_hours = fields.Integer('credits_hours', required=True)

    program_id = fields.Many2one('cms.program', 'Program Offered')

    semester_id = fields.Many2one('cms.semester', 'Semester')
    program_offer_line_ids = fields.One2many('cms.programoffer.line', 'program_offered_id',
                                             string='Program Offered Lines')


class CMSSemester(models.Model):
    _name = 'cms.semester'
    _description = 'Course Offered Semester Information'

    name = fields.Char('Name', required=True)

    program_offered_ids = fields.One2many('cms.program.offered', 'semester_id', string='Programs Offered')


class CMSProgramOfferLine(models.Model):
    _name = 'cms.programoffer.line'
    _description = 'Program Offered line Information'

    name = fields.Char('Name', required=True)
    duration = fields.Char('duration', required=True)
    semester = fields.Char('semester', required=True)
    course = fields.Char('course', required=True)

    program_offered_id = fields.Many2one('cms.program.offered', 'Program Offered')
    course_ids = fields.One2many('cms.course', 'program_offered_line_ids', string="programoffer line")


class CMSCourse(models.Model):
    _name = 'cms.course'
    _description = 'Course Information'

    course_code = fields.Char('course_code', required=True)
    name = fields.Char('Name', required=True)
    credits_hours = fields.Integer('credits_hours', required=True)
    prerequisites = fields.Char('prerequisites', required=True)

    program_line_id = fields.Many2one('cms.program.line', 'Program Line')
    program_offered_line_ids = fields.Many2one('cms.programoffer.line', 'Courses')
    prerequisite_ids = fields.One2many('cms.course.prerequisite', 'course_id', string='Prerequisites')

    course_offered_ids = fields.One2many('cms.course.offered', 'course_ids', string='course offered')


class CMSCoursePrerequisite(models.Model):
    _name = 'cms.course.prerequisite'
    _description = 'Course Prerequisite Information'

    name = fields.Char('Name', required=True)
    course_id = fields.Many2one('cms.course', 'Course', ondelete='cascade')


class CMSCourseOffered(models.Model):
    _name = 'cms.course.offered'
    _description = 'Course Offered Information'

    name = fields.Char('Name', required=True)
    credits_hours = fields.Integer('credits_hours', required=True)
    state = fields.Selection([('draft', 'Draft'), ('verified', 'Verified'), ('approved', 'Approved'),
                              ('cancelled', 'Cancelled')], 'Status', readonly=True, default="draft")
    course_ids = fields.Many2one('cms.course', 'course_offered')

    semester_session_ids = fields.Many2one('cms.semester.session', 'semester_session')


class CMSSemesterSession(models.Model):
    _name = 'cms.semester.session'
    _description = 'Semester Section Information'
    name = fields.Char('Name', required=True)
    course_offered_ids = fields.One2many('cms.course.offered', 'semester_session_ids', string='SemesterSession')
