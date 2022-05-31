# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
#    PedroGuirao pedro@serincloud.com
##############################################################################
from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = "account.move"

    donation_invoice_id = fields.Many2one('account.move', string='Donation invoice')

    def _create_donation_invoice(self):
        for record in self:
            if not record.donation_invoice_id.id:
              customer_journal = env['account.journal'].search([('type','=','sale')])[0]
              donation_invoice = env['account.move'].create({'move_type':'out_invoice', 'journal_id':customer_journal.id, 'partner_id':record.partner_id})
              record['donation_invoice_id'] = donation_invoice.id

              donation_invoice = record.donation_invoice_id
              donation_product = env['product.product'].search([('id','=',65)])
              for li in record.invoice_line_ids:
                if li.price_subtotal != 0:
                  name = " (" + str(li.quantity) + " x " + li.product_id.name +")"
                  donation_invoice['line_ids'] = [(0,0,{
                        'product_id':donation_product.id,
                        'name': donation_product.name + name,
                        'credit': abs(li.price_subtotal),
                        'account_id': donation_product.property_account_expense_id.id,
                        'analytic_account_id':li.analytic_account_id.id,
                        'partner_id': record.partner_id.id
                     }), (0, 0, {
                        'name': record.name or '/',
                        'debit': abs(li.price_subtotal),
                        'account_id': record.partner_id.property_account_receivable_id.id,
                        'partner_id': record.partner_id.id,
                        'exclude_from_invoice_tab':True
                     })]