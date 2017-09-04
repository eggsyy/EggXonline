# -*- coding: utf-8 -*-
import xadmin
from .models import CourseOrg, Teacher, CityDict

__author__ = 'Eggsy'
__date__ = '2017-08-24 19:51'


class CityDictAdmin(object):
    list_display = ['name', 'description', 'add_time']
    search_fields = ['name', 'description']
    list_filter = ['name', 'description', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'description', 'click_nums', 'fav_nums', 'address', 'city', 'add_time']
    search_fields = ['name', 'description', 'click_nums', 'fav_nums', 'address', 'city__name']
    list_filter = ['name', 'description', 'click_nums', 'fav_nums', 'address', 'city', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)

