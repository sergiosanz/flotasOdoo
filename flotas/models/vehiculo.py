# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class vehiculo(models.Model):
    _name = 'flotas.vehiculo'

    marca = fields.Char(String="marca")
    color = fields.Selection(selection=[('1', 'Blanco'), ('2', 'Gris'), ('3', 'Negro')])
    asientos = fields.Integer(String="asientos")
    idsconductores = fields.Many2Many(String= "conductores", comodel_name='flotas.conductor', relation = 'rel_vehiculos_conductores', column1='vehiculo', column2='conductor')
    idsviajes = fields.One2many('flotas.viaje', 'idvehiculo', String="viaje")
#   fecharevision = 