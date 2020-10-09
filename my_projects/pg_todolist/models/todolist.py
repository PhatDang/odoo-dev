# -*- coding: utf-8 -*-

from odoo import fields, models


class ToDoList(models.Model):
    _name = "to.do.list"
    -description = "Module TO DO LIST"

    tdl_name = fields.Char(
        required=True,
        string="Name",
    )
    tdl_type = fields.Selection([
        ('normal', 'Normal'),
        ('quickly', 'Quickly'),
        ('fast', 'Fast'),
        ('in_danger', 'Deadline'),
        ],
        default='normal',
        string="Type",
    )
