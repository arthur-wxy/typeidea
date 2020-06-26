#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：typeidea -> custom_site.py
@IDE    ：PyCharm
@Author ：ArthurWxy
@Date   ：2020/6/26 5:39 PM
@Desc   ：
=================================================="""
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
