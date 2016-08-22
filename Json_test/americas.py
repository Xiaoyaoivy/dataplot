# -*- coding: utf-8 -*-
import pygal
import pygal_maps_world.i18n

wm = pygal.maps.world.World()
wm.title = 'North,Central,and South America'

wm.add('North America', {'ca':1000, 'mx':123, 'us':213})
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')