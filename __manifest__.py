# -*- coding: utf-8 -*-
#############################################################################
#
#    kobros-tech Pvt. Ltd.
#
#    Copyright (C) 2020-TODAY kobros-tech(<https://www.linkedin.com/in/mohamed-alkobrosly/>).
#    Author: Mohamed Alkobrosli(<https://www.linkedin.com/in/mohamed-alkobrosly/>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': 'Invoice From Stock Picking Extension',
    'version': '16.0.1.0.0',
    'summary': """
    This module is an extension from Invoice From Stock Picking:
    https://apps.odoo.com/apps/modules/16.0/stock_move_invoice/#overview
    which can create create customer invoice,vendor bill, customer
    credit note and refund from stock picking.

    Custom Invoice From Stock Picking Extension is resposible for creating ONLY
    one invoice/bill for the multible selected transfers, 
    or even for the only one selected transfer.
    """,
    'description': 
    """In this module we solve bugs in the original one
    that we prevent creating more than one invoice/bill for each transfer.
    
    We provide a smart button in Sales Order/Purchase Order 
    that enables you to go to your created invoice directly.""",
    'category': 'Stock',
    'website': 'https://www.linkedin.com/in/mohamed-alkobrosly/',
    'license': "AGPL-3",
    'author': 'Abou Sajid (Mohamed Alkobrosli)',
    'company': 'kobros-tech',
    'maintainer': 'Mohamed Moustafa Alkobrosli',
    'summary': 'Prevent multible invoices/bills for the same transfers',
    'depends': [
        'stock_move_invoice',
        'sale',
        'purchase',
    ],
    'data': [
        'sale_purchase_views.xml',
    ],
}
