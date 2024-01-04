{
    "name": "hr leave type multi company",
    "summary": "Allow holidays type multi company management",
    "author": "Le Filament, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/multi-company",
    "version": "14.0.1.0.1",
    "license": "AGPL-3",
    "depends": ["hr_holidays"],
    "data": [
        "security/ir.model.access.csv",
        # datas
        "security/rule.xml",
        # views
        "views/hr_leave_type_view.xml",
        # views menu
        # wizard
    ],
    "qweb": [
        # "static/src/xml/*.xml",
    ],
    "installable": True,
    "auto_install": False,
}
