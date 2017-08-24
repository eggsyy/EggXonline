# -*- coding: utf-8 -*-
import xadmin
from .models import Course, Lesson, Video, CourseResource

__author__ = 'Eggsy'
__date__ = '2017-08-24 19:32'


class CourseAdmin(object):
    list_display = ['name', 'description', 'detail', 'degree', 'learn_time', 'students',
                    'fav_nums', 'click_num', 'add_time']
    search_fields = ['name', 'description', 'detail', 'degree', 'students', 'fav_nums', 'click_num']
    list_filter = ['name', 'description', 'detail', 'degree', 'learn_time', 'students',
                   'fav_nums', 'click_num', 'add_time']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
