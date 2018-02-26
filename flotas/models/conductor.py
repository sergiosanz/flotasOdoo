# -*- coding: utf-8 -*-

from odoo import models, fields, api

class conductor(models.Model):
    _name = 'flotas.conductor'
    _inherit = 'base.entidad'

    name = fields.Char(String="nombre")
    dni = fields.Integer(String="dni")
    idsvehiculos = fields.Many2Many(String= "conductor", comodel_name='flotas.vehiculo', relation = 'rel_vehiculos_conductores', column1='conductor', column2='vehiculo')