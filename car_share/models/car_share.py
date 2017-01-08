# -*- coding: utf-8 -*-
import datetime
import logging
from odoo import models, fields, api,_
from odoo.exceptions import Warning,ValidationError
_logger = logging.getLogger(__name__)
class CarDeparture(models.Model):
    _name = 'car.departure'
    _description = u"发车"
    name = fields.Char(u'单号', required=True, index=True, copy=False, default='New')
    departure_time = fields.Datetime(u'时间')
    start_point= fields.Many2one('car.point',u'起点',ondelete='restrict')
    end_point = fields.Many2one('car.point',u'终点',ondelete='restrict')
    seat_num = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],default='1',required=True,
                                   string=u'座位',readonly=False)
    mobile_phone = fields.Char(u'手机')
    remark = fields.Char(u'备注')
    details = fields.One2many('car.departure.detail','departure_id',u'途经站点')

    @api.model
    def create(self, vals):
        if not vals.get('name') or vals.get('name', 'New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('car.departure') or '/'
        return super(CarDeparture, self).create(vals)

    @api.constrains('departure_time')
    def _check_departure_time(self):
        departure_date = fields.Datetime.from_string(self.departure_time).date()
        now_date = datetime.datetime.now().date()
        if departure_date < now_date:
            raise ValidationError(_("不能选以前的时间"))

    @api.onchange('departure_time')
    def _onchange_departure_time(self):
        if self.departure_time:
            str_departure_time = self.departure_time
            departure_date = fields.Datetime.from_string(str_departure_time).date()
            now_time = datetime.datetime.today()
            # _logger.debug("----------------------",exc_info=True)
            now_date = datetime.datetime.now().date()
            # _logger.debug(now_time)
            # _logger.debug(now_date)
            if departure_date < now_date:
                raise Warning (_('不能选以前的时间'))
                return False


class CarDepartureDetail(models.Model):
    _name = 'car.departure.detail'
    _description = u'发车明细'
    departure_id = fields.Many2one('car.departure',u'发车记录',)
    point_name = fields.Many2one('car.point',u'站点')

class CarPoint(models.Model):
    _name = 'car.point'
    _description = u'站点名称'
    name = fields.Char(u'站点名称')
    _sql_constraints = [
        ('name_uniq',
         'UNIQUE (name)',
         u'名称已存在')
    ]

class CarSeat (models.Model):
    _name = 'car.seat'
    _description = u'乘坐信息'
    name = fields.Char(u'单号', required=True, index=True, copy=False, default='New')
    mobile_phone = fields.Char(u'手机')
    leave_time = fields.Datetime(u'时间')
    start_point = fields.Many2one('car.point', u'起点',ondelete='restrict')
    end_point = fields.Many2one('car.point',u'终点',ondelete='restrict')
    wait_point = fields.Many2one('car.point',u'候车点',ondelete='restrict')
    person_num = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],default='1',required=True,
                                   string=u'人數',readonly=False)
    remark = fields.Char(u'备注')

    @api.model
    def create(self, vals):
        if not vals.get('name') or vals.get('name', 'New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('car.seat') or '/'
        return super(CarSeat, self).create(vals)


    @api.returns('self')
    def default_car_seat_get(self):
        return self.env['car.seat'].search([('create_uid', '=', self.env.uid)], limit=1)

    @api.one
    @api.returns('self')
    def get_bill_no(self):
        bill_no = self.env['ir.sequence'].next_by_code('car.seat')
        return bill_no

    @api.constrains('leave_time')
    def _check_departure_time(self):
        if self.leave_time:
            leave_date = fields.Datetime.from_string(self.leave_time).date()
            now_date = datetime.datetime.now().date()
            if leave_date < now_date:
                raise ValidationError(_("不能选以前的时间"))

    @api.onchange('leave_time')
    def _onchange_departure_time(self):
        if self.leave_time:
            leave_date = fields.Datetime.from_string(self.leave_time).date()
            now_date = datetime.datetime.now().date()
            if leave_date < now_date:
                raise Warning (_('不能选以前的时间'))
                return False



