# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime, timedelta, date


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string="Title", required=True)
    author_id = fields.Many2one('library.author', string="Author")
    published_date = fields.Date(string="Published Date")
    book_age = fields.Integer(string="Book Age", compute='_compute_book_age')
    isbn = fields.Char(string="ISBN")
    page_count = fields.Integer(string="Number of pages")
    description = fields.Char(string="Description")

    @api.depends('published_date')
    def _compute_book_age(self):
        today = date.today()
        for record in self:
            if record.published_date:
                delta = today - record.published_date
                record.book_age = delta.days // 365
            else:
                record.book_age = 0

    @api.constrains('isbn')
    def _check_isbn_unique(self):
        for record in self:
            if self.env['library.book'].search_count([('isbn', '=', record.isbn)]) > 1:
                raise exceptions.ValidationError("ISBN must be unique.")

    @api.constrains('page_count')
    def _check_page_count_positive(self):
        for record in self:
            if record.page_count <= 0:
                raise exceptions.ValidationError(
                    "Number of pages must me positive")
