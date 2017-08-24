# -*- coding: utf-8 -*-
import xadmin
from xadmin import views

from .models import EmilVerifyRecord, Banner

__author__ = 'Eggsy'
__date__ = '2017-08-24 17:18'


class BaseSetting(object):
    pass
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'Eggsy后台管理系统'
    site_footer = 'Pumpkin ~'
    menu_style = 'accordion'


class EmilVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmilVerifyRecord, EmilVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
