from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    book_ids = fields.Many2many('library.book', string='Books Read')
