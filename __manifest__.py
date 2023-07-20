{
    'name': 'Pyament Transanction Stripe',
    'version': '1.0',
    'author': 'cybershop46',
    'category': 'Finanance',
    'summary': 'none',
    'description': """
    """,
    'depends': [
        'base',        
        'hr',
        'sale',
        'account',
        'purchase',
        'portal'
    ],
    'data': [
        'views/pt_payment_transaction_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',
    # 'post_init_hook': 'post_init_hook',
    # 'settings': 'my_module_settings',
}
