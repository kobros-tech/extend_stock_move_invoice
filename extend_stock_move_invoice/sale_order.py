# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SaleAdvancePaymentInv(models.TransientModel):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = 'sale.advance.payment.inv'

    # ---------------------------------------- Additional methods ------------------------------------

    def _create_invoices(self, sale_orders):

        for rec in self:
            for sale_order in rec.sale_order_ids:
                for transfer in sale_order.picking_ids:

                    # Prevent the method from creating more than single account.move record for each transfer
                    journals = transfer.env["account.move"].search([("transfer_ids", "=", transfer.id)])
                    if len(journals ) >= 1:
                        raise ValidationError(
                            f"There is already invoice/bill {journals.mapped('name')} for {transfer.name} Transfer")
        
        return super()._create_invoices(sale_orders)


class SaleOrder(models.Model):

        _inherit = 'sale.order'


        def action_view_extended_invoice(self):
            picking = self.picking_ids
            journals = self.env['account.move'].search([('transfer_ids', 'in', picking.mapped('id'))])
            return {
            'name': 'Invoices',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'domain': [('transfer_ids', 'in', picking.mapped("id"))],
            'context': {'create': False},
            'target': 'current'
            }
        
        