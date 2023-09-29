# -*- coding: utf-8 -*-
# from odoo import http


# class BookManagement(http.Controller):
#     @http.route('/book_management/book_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/book_management/book_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('book_management.listing', {
#             'root': '/book_management/book_management',
#             'objects': http.request.env['book_management.book_management'].search([]),
#         })

#     @http.route('/book_management/book_management/objects/<model("book_management.book_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('book_management.object', {
#             'object': obj
#         })
