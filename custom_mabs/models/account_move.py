# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
#    PedroGuirao pedro@serincloud.com
##############################################################################
from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = "account.move"

    donation_invoice_id = fields.Many2one('account.move', string='Donation invoice', copy=False)
