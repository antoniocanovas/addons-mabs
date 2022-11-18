# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
#    PedroGuirao pedro@serincloud.com
##############################################################################

{
    "name": "Custom Mabs",
    "version": "14.0.1.0.0",
    "category": "Contracts/Purchases",
    "author": "Serincloud",
    "maintainer": "Serincloud",
    "website": "www.ingenieriacloud.com",
    "license": "AGPL-3",
    "depends": [
        "purchase",
    ],
    "data": [
        "data/server_actions.xml",
        "views/purchase_order_legal_report.xml",
        "views/donation_report.xml",
        "views/purchase_order.xml",
        "views/sale_order.xml",
        "views/res_company.xml",
        "views/account_move.xml",
    ],
    "installable": True,
}
