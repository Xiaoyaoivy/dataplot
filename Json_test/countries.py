# -*- coding: utf-8 -*-
# from pygal.maps.world import COUNTRIES
# from pygal_maps_world import i18n
from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print country_code,COUNTRIES[country_code]