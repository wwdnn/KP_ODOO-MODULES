from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResBus(models.Model):
    _name = 'res.bus'
    _description = 'Bus'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _sql_constraints = [
        ('bus_code_uniq', 'unique(code)', 'Nomor Kode Bus harus berbeda !')
    ]

    name = fields.Char(string='Name', tracking=True)
    code = fields.Char(string='Code', tracking=True)
    capacity = fields.Integer(string='Capacity', tracking=True)
    image = fields.Binary(string='Image', tracking=True)
    # state selection
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("ready", "Ready"),
            ("mt", "Maintenance"),
            ("depr", "Deprecated"),
        ],
        string="Status",
        default="draft",
        tracking=True,
    )