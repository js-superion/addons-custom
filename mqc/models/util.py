# -*- coding: utf-8 -*-
import datetime, pytz
from openerp import models, fields,api
class utils(models.Model):
    # def __init__(self,name):
    #     self.name = name;
    def get_zero_time(self):
        '''
        获取当前时区的utc时间
        :return:
        '''
        now_time = datetime.datetime.today()
        tz = self.env.user.tz or 'Asia/Shanghai'
        tz_timedelta = now_time.replace(tzinfo=pytz.timezone('UTC')) - now_time.replace(tzinfo=pytz.timezone(tz))
        zero_time = now_time - tz_timedelta
        zero_time = zero_time.replace(tzinfo=pytz.timezone('UTC'))
        return zero_time

