#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：typeidea -> adminforms.py
@IDE    ：PyCharm
@Author ：ArthurWxy
@Date   ：2020/6/26 5:18 PM
@Desc   ：
=================================================="""
from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
