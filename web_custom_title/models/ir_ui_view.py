# -*- coding: utf-8 -*-
import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class View(models.Model):
    _inherit = 'ir.ui.view'

    @api.model
    def render_template(self, template, values=None, engine='ir.qweb'):
        if template in ['web.login', 'web.webclient_bootstrap']:
            if not values:
                values = {}
            values["title"] = self.env['ir.config_parameter'].sudo().get_param("web.base.title", "")
        return super(View, self).render_template(template, values=values, engine=engine)