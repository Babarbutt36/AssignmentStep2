from odoo import models, fields
class Course(models.Model):
     _name = 'openacademy.course'
     _description = 'course is the model of openacademy module'
     name = fields.Char(string="Title", required=True)
     description = fields.Char(String= "Course Description")
     resposible_id = fields.Many2one('res.users',ondelete='set null')
     session_ids = fields.One2many('openacademy.session','course_id',String='Sessions')
     _sql_constraints = [
           ('check_name_and_description','CHECK(name != description)','Title and Description cant be same'),
           ('unique_name', 'UNIQUE(name)', 'Course name must have to be unique')
     ]



