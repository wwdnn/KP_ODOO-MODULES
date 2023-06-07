from odoo import models, fields, api, _
from odoo.exceptions import UserError

class NamaModel(models.Model):
    _name = 'nama.model'
    _description = ''

    name = fields.Char(string='Label dari Field')
    fo_da