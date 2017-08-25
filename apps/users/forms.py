# -*- coding: utf-8 -*-
__author__ = 'Eggsy'
__date__ = '2017-08-25 15:25'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
