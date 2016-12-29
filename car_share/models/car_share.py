# -*- coding: utf-8 -*-

from openerp import models, fields, api

class CarDeparture(models.Model):
    _name = 'car.departure'
    _description = u"发车"
    name = fields.Char(u'单号', required=True, index=True, copy=False, default='New')
    departure_time = fields.Datetime(u'时间')
    start_point= fields.Many2one('car.point',u'起点')
    end_point = fields.Many2one('car.point',u'终点')
    seat_num = fields.Integer(u'座位')
    mobile_phone = fields.Char(u'手机')
    remark = fields.Char(u'备注')
    details = fields.One2many('car.departure.detail','departure_id',u'途经站点')

    @api.model
    def create(self, vals):
        if not vals.get('name') or vals.get('name', 'New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('car.departure') or '/'
        return super(CarDeparture, self).create(vals)




class CarDepartureDetail(models.Model):
    _name = 'car.departure.detail'
    _description = u'发车明细'
    departure_id = fields.Many2one('car.departure',u'发车记录',)
    point_name = fields.Many2one('car.point',u'站点')

class CarPoint(models.Model):
    _name = 'car.point'
    _description = u'站点名称'
    name = fields.Char(u'站点名称')

class CarSeat (models.Model):
    _name = 'car.seat'
    _description = u'乘坐信息'
    name = fields.Char(u'单号', required=True, index=True, copy=False, default='New')
    mobile_phone = fields.Char(u'手机')
    leave_time = fields.Datetime(u'时间')
    start_point = fields.Many2one('car.point', u'起点')
    end_point = fields.Many2one('car.point',u'终点')
    wait_point = fields.Many2one('car.point',u'候车点')
    person_num = fields.Integer(u'人数')
    remark = fields.Char(u'备注')

    @api.model
    def create(self, vals):
        if not vals.get('name') or vals.get('name', 'New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('car.seat') or '/'
        return super(CarSeat, self).create(vals)

