# -*- coding: utf-8 -*-
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """指定国家返回pygal使用的两个字母的国别码"""
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code

    #如果没有找到,返回none
    return None