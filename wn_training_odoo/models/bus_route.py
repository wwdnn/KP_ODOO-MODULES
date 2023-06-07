from odoo import models, fields, api, _
from odoo.exceptions import UserError

class BusRoute(models.Model):
    _name = 'bus.route'
    _description = 'Bus Route'

    name = fields.Char(string='Name')