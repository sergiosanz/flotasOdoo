# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta,date,datetime

class viaje(models.Model):
    _name = 'flotas.viaje'

    idvehiculo = fields.Many2one('flotas.vehiculo', String="vehiculo")
    provorigen = fields.One2many(String="origen")
    provdestino = fields.One2many(String="destino")
    fecha = fields.Date(String="fecha")
    duracionhoras = fields.Integer(String="horas")
#   más2horas = 