# -*- coding:utf-8 -*-
__author__ = 'zy'
__date__ = '2018/6/16'

import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views

# 创建admin的管理类,这里不再是继承admin，而是继承object
class EmailVerifyRecordAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 配置筛选字段
    list_filter = ['code', 'email', 'send_type', 'send_time']


# 创建banner的管理类
class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']


# 创建xadmin的全局管理器并与view绑定
class BaseSetting(object):
    # 开启主体功能
    enable_themes = True
    use_bootswatch = True


# xadmin全局配置参数信息设置
class GlobalSettings(object):
    site_title = "zy'demo"
    site_footer = "zy"
    # 收起菜单
    menu_style = "accordion"



xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# 将全局配置管理与view绑定注册
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)