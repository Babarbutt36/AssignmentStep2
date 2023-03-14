from odoo import models, fields,api
from odoo.exceptions import ValidationError
class Session(models.Model):
     _name = 'openacademy.session'
     _description = 'session is the model of openacademy module'
     name =fields.Char(string="Session name")
     date = fields.Date(String= "Session Date",default=fields.Date.context_today)
     duration = fields.Float(digits =(6, 2), help="Duration in days")
     seats = fields.Integer(String ="Number of Seats")
     instructor_id =fields.Many2one('res.partner',string='Instructor')
     course_id = fields.Many2one('openacademy.course',required=True)
     attendees_ids = fields.Many2many('res.partner',String ='Attendees')
     taken_seats = fields.Float(String='Seat Taken',compute='_compute_taken_seats')
     active =fields.Boolean(default=True)


     @api.constrains('instructor_id','attendees_ids')
     def _instructor_not_attendess(self):
          for record in self:
               if record.instructor_id.id in record.attendees_ids.ids:
                    raise ValidationError("Cant have Instructor as Attendees")


     @api.onchange('attendees_ids', 'seats')
     def _onchange_price(self):
          if self.seats < 0:
               return {
                    'warning': {
                         'title': "Something bad happened",
                         'message': "Seats cant be negative",
                    }
               }

          if len(self.attendees_ids) > self.seats:
               return {
                    'warning': {
                         'title': "Something bad happened",
                         'message': "you cant have more attendees than Seats",
                    }
               }

     @api.depends('attendees_ids', 'seats')
     def _compute_taken_seats(self):
          for session in self:
               if session.seats == 0:
                    session.taken_seats == 0
               else:
                    session.taken_seats = (len(session.attendees_ids) / session.seats) * 100
