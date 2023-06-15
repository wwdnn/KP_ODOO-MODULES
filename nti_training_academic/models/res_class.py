from odoo import models, fields, api

class ResClass(models.Model):
    _name = 'class.class'
    _desctription = 'Kelas yang dapat diambil oleh mahasiswa atau dosen'

    name = fields.Char(string='Name')
    date = fields.Date(string='Date')
    user_id = fields.Many2one(
        comodel_name='res.users',
        string="Responsible",
        required=True, 
    )
    student_ids = fields.Many2many(
        string='Student',
        comodel_name='res.partner',
    )
    subject_line_ids = fields.One2many(
        string='Subject(s)',
        comodel_name='subject.line',
        inverse_name='class_id',
    )
    
    