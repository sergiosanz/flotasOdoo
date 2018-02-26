# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta,date,datetime

class seguro(models.Model):
    _inherit = 'base.empresa'

    name = fields.Char(string='nombre', required=True, help='nombre de la compañia')
    fechadevencimiento = fields.Date(string='fecha de vencimiento', required=True)
    # (1)seguro (1)coche las normas son calras
    vehiculo_id = fields.One2Many('flotas.vehiculo', ondelete='set null', string="Vehicle", index=True)