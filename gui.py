import bpy

def get_lights_objects(scene):
    light_list=[]
    for obj in scene.objects:
        if obj.type=='LIGHT':
            light_list.append(obj)
    return light_list

def return_light_icon(data):
    return 'LIGHT_%s' % data.type

def get_selection_icon(ob,context):
    if ob.select_get():
        if context.view_layer.objects.active==ob:
            return "PROP_CON"
        else:
            return "RADIOBUT_ON"
    else:
        return "RADIOBUT_OFF"


class LIGHTHELPER_PT_manager(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Lights"
    bl_label = "Light Manager"

    def draw(self, context):
        layout = self.layout

        split=layout.split(align=True,factor=0.4)
        col1=split.column(align=True)
        col2=split.column(align=True)
        split=col2.split(align=True)
        col2=split.column(align=True)
        col3=split.column(align=True)
        col3.scale_x=0.9

        lights=get_lights_objects(context.scene)
        for light in lights:

            #col1.label(text=light.name, icon=return_light_icon(light.data))
            row=col1.row(align=True)
            props=light.lighthelper_object_properties
            if props.hide_panel:
                icon="RIGHTARROW_THIN"
            else:
                icon="DOWNARROW_HLT"
            row.prop(
                props,
                'hide_panel',
                text="",
                icon=icon,
                emboss=False,
            )
            row.label(text="",icon=get_selection_icon(light,context))
            op=row.operator(
                'lighthelper.select_light',
                text=light.name,
                icon=return_light_icon(light.data),
                emboss=False,
            )
            op.light_name=light.name
            
            row=col2.row(align=True)
            row.alignment="EXPAND"
            sub=row.row(align=True)
            sub.scale_x=0.25
            sub.prop(light.data, 'color', text="")
            row.prop(light.data, 'energy', text="")
            
            row=col3.row(align=True)
            row.alignment="RIGHT"
            row.prop(light, 'hide_select', text="", emboss=False)
            row.prop(light, 'hide_viewport', text="", emboss=False)
            row.prop(light, 'hide_render', text="", emboss=False)

def register():
    bpy.utils.register_class(LIGHTHELPER_PT_manager)

def unregister():
    bpy.utils.unregister_class(LIGHTHELPER_PT_manager)