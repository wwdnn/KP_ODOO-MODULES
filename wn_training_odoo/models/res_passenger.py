from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPassenger(models.Model):
    _name = 'res.passenger'
    _description = 'Passenger'

    name = fields.Char(string='Name')
    weight = fields.Float(string='Weight(Kg)')
    height = fields.Float(string='Height(Cm)')
    born_date = fields.Date(string='Born Date')