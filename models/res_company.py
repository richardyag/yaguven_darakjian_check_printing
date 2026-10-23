from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    account_check_printing_layout = fields.Selection(
        selection_add=[
            (
                "yaguven_darakjian_check_printing.action_print_blank_check_bottom_full",
                "Print Blank Check (Bottom) + Invoice Stub - Darakjian",
            ),
        ],
        ondelete={
            "yaguven_darakjian_check_printing.action_print_blank_check_bottom_full": "set default",
        },
    )
