# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class StockPicking(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------
    
    _inherit = 'stock.picking'
    
    # ---------------------------------------- Additional methods ------------------------------------
    
    def check_validity(self):

        for transfer in self:

            # Prevent the method from creating more than single account.move record for each transfer
            journals = transfer.env["account.move"].search([("transfer_ids", "=", transfer.id)])
            if len(journals ) >= 1:
                raise ValidationError(f"There is already invoice/bill {journals.mapped('name')} for {transfer.name} Transfer")

            # Prevent the method from creating any account.move record if there is a sale oreder invoice
            sale_invoice = transfer.sale_id.invoice_ids
            if len(sale_invoice) >= 1:
                raise ValidationError(
                    f"There is already sale order invoice {sale_invoice.mapped('name')} for {transfer.name} transfer")

            # Prevent the method from creating any account.move record if there is a purchase oreder bill
            purchase_bill = transfer.purchase_id.invoice_ids
            if len(purchase_bill) >= 1:
                raise ValidationError(
                    f"There is already purchase order bill {purchase_bill.mapped('name')} for {transfer.name} transfer")

            # Change state of Sale or Pruchase
            if len(transfer.sale_id) > 0 and transfer.sale_id.invoice_count == 0:
                transfer.sale_id.write(
                    {"invoice_status": "invoiced"})
            elif len(transfer.purchase_id) > 0 and transfer.purchase_id.invoice_count == 0:
                transfer.purchase_id.write(
                    {"state": "purchase"})
                print("**************purchased*************************")


    def create_invoice(self):
        self.check_validity()
        return super().create_invoice()
    

    def create_bill(self):
        self.check_validity()
        return super().create_bill()
    

    def create_customer_credit(self):
        self.check_validity()
        return super().create_customer_credit()
    

    def create_vendor_credit(self):
        self.check_validity()
        return super().create_vendor_credit()
    

    def action_create_multi_invoice_for_multi_transfer(self):
        self.check_validity()
        return super().action_create_multi_invoice_for_multi_transfer()
    
    
    class PurchaseOrder(models.Model):

        # ---------------------------------------- Private Attributes ---------------------------------

        _inherit = "purchase.order"
        
        # ---------------------------------------- Action methods ------------------------------------

        def action_create_invoice(self):
            
            for transfer in self.picking_ids:
                # Prevent the method from creating more than single account.move record for each transfer
                journals = transfer.env["account.move"].search([("transfer_ids", "=", transfer.id)])
                if len(journals ) >= 1:
                    raise ValidationError(
                        f"There is already invoice/bill {journals.mapped('name')} for {transfer.name} Transfer")
            
            return super().action_create_invoice()
        

        def action_view_extended_invoice(self):
            picking = self.picking_ids
            journals = self.env['account.move'].search([('transfer_ids', 'in', picking.mapped("id"))])
            return {
            'name': 'Invoices',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'domain': [('transfer_ids', 'in', picking.mapped("id"))],
            'context': {'create': False},
            'target': 'current'
            }