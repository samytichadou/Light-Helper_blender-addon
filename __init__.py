'''
Copyright (C) 2018 Samy Tichadou (tonton)
samytichadou@gmail.com

Created by Samy Tichadou

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Light Helper",
    "description": "Manage several Lights quickly",
    "author": "Samy Tichadou (tonton)",
    "version": (0, 2, 0),
    "blender": (3, 0, 0),
    "location": "",
    "wiki_url": "https://github.com/samytichadou/Light-Helper_blender-addon/blob/master/README.md",
    "tracker_url": "https://github.com/samytichadou/Light-Helper_blender-addon/issues/new",
    "category": "Lighting" }

# IMPORT SPECIFICS
##################################

from . import   (
    gui,
    select_light_operator,
    isolate_light_operator,
    properties,
)


# register
##################################

def register():
    gui.register()
    select_light_operator.register()
    isolate_light_operator.register()
    properties.register()

def unregister():
    gui.unregister()
    select_light_operator.unregister()
    isolate_light_operator.unregister()
    properties.unregister()