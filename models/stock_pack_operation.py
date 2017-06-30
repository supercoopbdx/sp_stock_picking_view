# -*- coding: utf-8 -*-

from openerp import models, fields, api

import openerp.addons.decimal_precision as dp

class StockPackOperation(models.Model):
    _inherit = 'stock.pack.operation'

    # @api.onchange('name','product_id','move_line_tax_ids','product_uom_qty')

    # first_seller_id = product_id.seller_ids[0]
    standard_price = fields.Float(string="Supplier Price Per Unit", store=True, readonly=False, related="product_id.standard_price")
