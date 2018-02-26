# -*- coding: utf-8 -*-

from odoo import models, fields, api

class provincia(models.Model):
    _name = 'flotas.provincia'

    name = fields.Char(String="nombre")