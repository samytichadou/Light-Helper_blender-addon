import bpy

def get_lights_objects(scene):
    light_list=[]
    for obj in scene.objects:
        if obj.type=='LIGHT':
            light_list.append(obj)
    return light_list

def return_light_icon(data):
    return 'LIGHT_%s' % data.type

class LIGHTHELPER_PT_manager(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Lights"
    bl_label = "Light Manager"

    def draw(self, context):
        layout = self.layout
        col=layout.column(align=True)
        lights=get_lights_objects(context.scene)
        for light in lights:
            row=col.row(align=True)
            row.label(text=light.name, icon=return_light_icon(light.data))
            row.prop(light.data, 'color', text="")
            row.prop(light.data, 'energy', text="")
            row.prop(light, 'hide_select', text="", emboss=False)
            row.prop(light, 'hide_viewport', text="", emboss=False)
            row.prop(light, 'hide_render', text="", emboss=False)

def register():
    bpy.utils.register_class(LIGHTHELPER_PT_manager)

def unregister():
    bpy.utils.unregister_class(LIGHTHELPER_PT_manager)