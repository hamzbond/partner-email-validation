# -*- coding: utf-8 -*-
from validate_email import validate_email
from odoo import api, models, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('email')
    def _check_email(self):
        """
        Check the email is valid or not
        """
        if self.email:
            is_valid = validate_email(self.email, check_mx=False, verify=True, debug=False, smtp_timeout=10)
            if is_valid is not True:
                raise ValidationError(_('"%s" is invalid email address or does not exist.') % self.email)
