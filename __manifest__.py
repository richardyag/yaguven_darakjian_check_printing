{
    "name": "Darakjian - Blank Check with Invoice Stub",
    "version": "19.0.1.0.0",
    "summary": "Adds the invoice stub table to Odoo's native Blank Check (Bottom) layout",
    "description": """
Odoo's native "Print Blank Check (Bottom)" layout draws the bank name, routing/account
MICR line, company address and signature line, but its stub (the voucher area above the
check) only prints the company name -- it has no table of which bill(s) the check is
paying. The native "Print Check (Bottom)" layout has that table, but does not draw the
bank/MICR/signature block, since it assumes pre-printed check stock.

This module adds a THIRD option, with both: the blank check face plus the invoice stub
table. It is purely additive -- the two original Odoo layouts are untouched and still
selectable, in case the pre-printed-stock layout is ever needed again.
    """,
    "category": "Accounting",
    "author": "Yaguven C.G.",
    "depends": ["l10n_us_check_printing"],
    "data": [
        "reports/check_stub_blank_full_templates.xml",
        "reports/check_report_actions.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
