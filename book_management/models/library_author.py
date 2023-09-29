from odoo import models, fields, api


class LibraryAuthor(models.Model):
    _name = "library.author"
    _description = "Book Author"

    name = fields.Char(string="Name", required=True)
    birth_date = fields.Date(string="Birth Date")
    nationality = fields.Char(string="Nationality")
