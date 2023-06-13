from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPassenger(models.Model):
    _name = 'res.passenger'
    _description = 'Passenger'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    weight = fields.Float(string='Weight(Kg)', tracking=True)
    height = fields.Float(string='Height(Cm)', tracking=True)
    born_date = fields.Date(string='Born Date', tracking=True)
    gender = fields.Selection([("man","Man"),("woman","Woman")], string='Gender', tracking=True)