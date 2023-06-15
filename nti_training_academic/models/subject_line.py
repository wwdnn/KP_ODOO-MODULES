from odoo import models, fields, api

class SubjectLine(models.Model):
    _name = 'subject.line'
    _description = 'Penjelasan mata kuliah beserta dosen pengampu dan jam kuliah'

    subject_id = fields.Many2one(
        comodel_name='subject.subject',
        string="Subject",
        required=True, 
    )
    lecturer_id = fields.Many2one(
        comodel_name='res.partner',
        string="Lecturer",
        related="subject_id.lecturer_id",
    )
    class_id = fields.Many2one(
        comodel_name='class.class',
        string="Class",
    )
    start_hour = fields.Float(string='Start Hour')
    end_hour = fields.Float(string='End Hour')