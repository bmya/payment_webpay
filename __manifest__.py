# -*- coding: utf-8 -*-

{
    'name': 'Webpay Payment Acquirer',
    'category': 'Payment / Chile',
    'author': 'Daniel Santibáñez Polanco',
    'summary': 'Payment Acquirer: Chilean Webpay Implementation',
    'website': 'https://odoocoop.cl',
    'version': "1.4.0",
    'description': """Chilean Webpay Payment Acquirer""",
    'depends': [
                'payment',
                'payment_currency',
                'sale_payment',
            ],
    'external_dependencies': {
        'python': [
            'suds',
            'xmlsec',
            'urllib3',
            # En Debian/Ubuntu:
            # sudo apt-get install libssl-dev libxml2-dev libxmlsec1-dev
            #    Sistemas basados en RedHat:
            # sudo yum install openssl-devel libxml2-devel xmlsec1-devel xmlsec1-openssl-devel libtool-ltdl-devel
        ],
    },
    'data': [
        'views/webpay.xml',
        'views/payment_acquirer.xml',
        'views/payment_transaction.xml',
        'views/website_sale_template.xml',
        'data/webpay.xml',
    ],
    'installable': True,
    'application': True,
}
