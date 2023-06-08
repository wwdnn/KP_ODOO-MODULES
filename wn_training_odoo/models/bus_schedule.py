from odoo import models, fields, api, _
from odoo.exceptions import UserError

class BusSchedule(models.Model):
    _name = 'bus.schedule'
    _description = 'Schedule'

    name = fields.Char(string='Name', default="New", readonly=True)
    schedule = fields.Datetime(string="Schedule")
    payment_type = fields.Selection([("cash","Cash"),("transfer","Transfer")], string='Payment')
    departure = fields.Datetime(string="Departure")
    arrival = fields.Datetime(string="Arrival")
    bus_id = fields.Many2one(
        comodel_name='res.bus',
        string='Bus',
    )
    route_id = fields.Many2one(
        comodel_name='bus.route',
        string='Route',
    )
    baggage_line_ids = fields.One2many(
        comodel_name='baggage.baggage',
        inverse_name='schedule_id',
        string='Baggage(s)',
    )
    passenger_ids = fields.Many2many(
        comodel_name='res.passenger', 
        string='Passenger(s)'
    )
    capacity = fields.Integer(
        string='Capacity',
        related='bus_id.capacity',
    )

    @api.model
    def create(self, values):
        result = super(BusSchedule, self).create(values)

        result['name'] = self.env['ir.sequence'].next_by_code('bus.schedule.sequence')

        return result


class Baggage(models.Model):
    _name = 'baggage.baggage'
    _description = 'Baggage of Passenger'

    name = fields.Char(string='Name')
    weight = fields.Float(string='Weight(Kg)')
    schedule_id = fields.Many2one(
        comodel_name='bus.schedule',
        string='Schedule',
    )