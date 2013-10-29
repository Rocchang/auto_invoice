# -*- coding: utf-8 -*-

from osv import fields, osv


class sale_order(osv.osv):
    _inherit = "sale.order"

    _columns = {
         
             'order_policy': fields.selection([
                  ('manual', 'Auto Invioce'),
                  ('picking', 'On Delivery Order'),
                  ('prepaid', 'Before Delivery'),
            ], 'Create Invoice', required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
            help="""On demand: A draft invoice can be created from the sales order when needed. \nOn delivery order: A draft invoice can be created from the delivery order when the products have been delivered. \nBefore delivery: A draft invoice is created from the sales order and must be paid before the products can be delivered."""),    
    }
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
