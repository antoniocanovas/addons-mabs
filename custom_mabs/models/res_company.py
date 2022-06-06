# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
#    PedroGuirao pedro@serincloud.com
##############################################################################
from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = "res.company"

    donation_product_id = fields.Many2one('product.product', string='Donation product')
    donation_journal_id = fields.Many2one('account.journal', string='Donation journal')
