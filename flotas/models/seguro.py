# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta,date,datetime

class seguro(models.Model):
    _inherit = 'base.enterprise'

    name = fields.Char(String="nombre")
    fechavencimiento = fields.Date(String="fechadevencimiento")