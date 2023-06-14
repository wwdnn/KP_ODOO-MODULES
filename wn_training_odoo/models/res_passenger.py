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
    age = fields.Integer(string='Age', tracking=True, compute="_count_age");
    gender = fields.Selection([("man","Man"),("woman","Woman")], string='Gender', tracking=True)

    
    @api.depends('born_date')
    def _count_age(self):
        for rec in self:
            if rec.born_date:
                rec.age = (fields.Date.today() - rec.born_date).days / 365
            else:
                rec.age = 0
    
    
    