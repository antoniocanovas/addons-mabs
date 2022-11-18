# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
#    PedroGuirao pedro@serincloud.com
##############################################################################

{
    "name": "Purchase donation",
    "version": "14.0.1.0.0",
    "category": "Purchase",
    "author": "www.serincloud.com",
    "maintainer": "Serincloud",
    "website": "www.serincloud.com",
    "license": "AGPL-3",
    "depends": [
        'base_automation',
        'purchase',
        'stock',
        'account',
        'analytic',
    ],
    "data": [
        "views/purchase_order_views.xml",
        "views/product_template_views.xml",
        "views/menu_views.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
}