from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResBus(models.Model):
    _name = 'res.bus'
    _description = 'Bus'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    capacity = fields.Integer(string='Capacity')
    image = fields.Binary(string='Image')