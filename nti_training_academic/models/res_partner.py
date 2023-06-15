from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    birthday = fields.Date(string='Birthday')
    age = fields.Integer(string="Age", compute="_count_age")
    is_lecturer = fields.Boolean(string='Lecturer', store=True,)
    subject_line_ids = fields.One2many(
        string='Subject(s)',
        comodel_name='subject.subject',
        inverse_name='lecturer_id',
    )

    def button_subjects(self):
        return {
            'name': 'Subjects',
            'view_mode': 'tree,form',
            'res_model': 'subject.subject',
            'domain': [('lecturer_id', '=', self.id)],
            'type': 'ir.actions.act_window',
        }

    
    @api.depends('birthday')
    def _count_age(self):
        for rec in self:
            if rec.birthday:
                rec.age = (fields.Date.today() - rec.birthday).days / 365
            else:
                rec.age = 0
    
    






    

    