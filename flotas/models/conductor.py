# -*- coding: utf-8 -*-

from odoo import models, fields, api

class conductor(models.Model):
    _name = 'flotas.conductor'
    _inherit = 'base.entidad'

    name = fields.Char()
    dni = 