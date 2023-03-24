from odoo import fields, models


class ShowWizard(models.TransientModel):
    _name = 'show.wizard'
    _description = 'Show Wizard'

    price_plus = fields.Integer('Price Plus', default=lambda self: self.env['show.showroom'].browse(
        self.env.context.get('active_id')).price)

    def add(self):
        self.env['show.showroom'].browse(self.env.context.get('active_id')).write({'price': self.price_plus})
        return {'type': 'ir.actions.act_window_close'}