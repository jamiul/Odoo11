# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountInvoice(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'
    
    
    month = fields.Selection(
       [('1', 'January'), ('2', 'February'), ('3', 'March '),('4', 'April'),('5', 'May '),('6', 'June'),
        ('7', 'July'),('8', 'August'),('9', 'September'),('10', 'October'), ('11', 'November'),
       ('12', 'December ')], 'Tution Month')
    
    items= fields.Char('Items' )