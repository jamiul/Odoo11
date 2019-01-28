# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import logging

from _cffi_backend import string

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT

_logger = logging.getLogger(__name__)


class AttendanceRecapReportWizard(models.TransientModel):
    _name = 'attendance.recap.report.wizard'

    date_start = fields.Date(string="Start Date", required=True, default=fields.Date.today)
    date_end = fields.Date(string="End Date", required=True, default=fields.Date.today)
    customer_id = fields.Many2one('res.partner', string='Customer Name')

    @api.multi
    def get_report(self):
        """Call when button 'Get Report' clicked.
        """
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'customer_id': self.customer_id.id,
                'customer_name': self.customer_id.name,
                'date_start': self.date_start,
                'date_end': self.date_end,
                # 'invoice_status': self.invoice_status,
            },
        }

        # use `module_name.report_id` as reference.
        # `report_action()` will call `get_report_values()` and pass `data` automatically.
        return self.env.ref('cj_custom_report.recap_report').report_action(self, data=data)


class ReportAttendanceRecap(models.AbstractModel):
    """Abstract Model for report template.

    for `_name` model, please use `report.` as prefix then add `module_name.report_name`.
    """

    _name = 'report.cj_custom_report.attendance_recap_report_view'

    @api.model
    def get_report_values(self, docids, data=None):
        date_start = datetime.strptime(data['form']['date_start'], DATE_FORMAT)
        date_end = datetime.strptime(data['form']['date_end'], DATE_FORMAT) + timedelta(days=1)
        customer_id = data['form']['customer_id']
        customer_name = data['form']['customer_name']
        
        _logger.info(customer_id)
        
        date_diff = (date_end - date_start).days

        docs = []
        # partners = self.env['res.partner'].search([('partner_id', '=', customer_name)], order='name asc')
        # invoice = self.env['account.invoice'].search([('partner_id', '=', id.customer_name)])
        # partner_id = self.env['res.partner']._find_accounting_partner(invoice.partner_id).id
        invoices = self.env['account.invoice'].search([
            ('partner_id', '=', customer_id),
            ('date_invoice', '>=', date_start.strftime(DATETIME_FORMAT)),
            ('date_invoice', '<', date_end.strftime(DATETIME_FORMAT))])
        # sessions = self.env['openacademy.session'].search([], order='name asc')
        
        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start.strftime(DATE_FORMAT),
            'date_end': (date_end - timedelta(days=1)).strftime(DATE_FORMAT),
            'customer_id': data['form']['customer_id'],
            'customer_name': customer_name,
            'invoices': invoices,
            
        }
