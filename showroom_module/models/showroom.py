from odoo import fields, models


class Showroom(models.Model):
    _name = 'show.showroom'
    name = fields.Char(string="Model Name")
    brand = fields.Char(string="Brand Name")
    fuel_type = fields.Selection(([('petrol', 'Petrol'), ('diesel', 'Diesel'), ('ev', 'EV')]), string='Fuel Type',
                                 default='petrol')
    year = fields.Integer(string='Year')
    price=fields.Integer(string='Price')