# -*- coding: utf-8 -*-
{
    'name': "Email Address Validation on Partner",
    'version': '14.0.1.0.0',
    'category': 'Discuss',
    'summary': """Check Whether A Given Email Address Is Valid Or Not""",
    'description': """Check Whether A Given Email Address Is Valid Or Not In Partner Form""",
    'author': "hamzbond",
    'company': "bond",
    'maintainer': 'hamzbond',
    'website': "https://www.hamzbond.github.io",
    'depends': [
        'base',
        'contacts'
    ],
    'external_dependencies': {'python': ['validate_email', 'py3DNS']},
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
