# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Own_Task',
    'version' : '1.2',
    # 'summary': 'Invoices & Payments',
    'sequence': 10,
    'description': """
Invoicing & Payments
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    # 'category': 'Accounting/Accounting',
    # 'website': 'https://www.odoo.com/app/invoicing',
    # 'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['sale_management'],
    'data': [
    'security/own_task_security.xml',
    'security/ir.model.access.csv',
    'views/menu.xml',
    'views/server_action.xml',
    'views/inherit_menu_action.xml',
    'views/res_config_views.xml',
    'views/seqeunce_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    # 'post_init_hook': '_account_post_init',
    
    'license': 'LGPL-3',
}
