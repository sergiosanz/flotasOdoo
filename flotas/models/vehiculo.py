# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vehiculo(models.Model):
    _name = 'flotas.vehiculo'

    marca = fields.Char()
    color = 
    asientos fields.Integer()
    idsconductores = fields.Many2Many(string= "conductores", comodel_name='flotas.conductor', )