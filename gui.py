import bpy

def get_lights_objects(context):
    light_list=[]
    for obj in context.view_layer.objects:
        if obj.type=='LIGHT':
            light_list.append(obj)
    return light_list

def return_light_icon(data):
    return 'LIGHT_%s' % data.type

def get_selection_icon(ob,context):
    isolated_light=context.scene.lighthelper_scene_properties.isolated_light
    if isolated_light is not None:
        if ob==isolated_light:
            return "OUTLINER_OB_LIGHT"
        else:
            return "DOT"
    if context.view_layer.objects.active==ob:
        if ob.select_get():
            return "PROP_CON"
        else:
            return "PROP_OFF"
    elif ob.select_get():
        return "RADIOBUT_ON"
    else:
        return "RADIOBUT_OFF"


class LIGHTHELPER_PT_manager(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Lights"
    bl_label = "Light Manager"

    def draw(self, context):
        isolated_light=context.scene.lighthelper_scene_properties.isolated_light
        layout = self.layout

        col=layout.column(align=True)

        lights=get_lights_objects(context)
        for light in lights:
            not_isolated=False
            if isolated_light is not None and isolated_light!=light:
                not_isolated=True

            #box=col.box()
            row=col.row(align=True)

            # Light Subpanel display toggle
            props=light.lighthelper_object_properties
            if props.hide_panel:
                icon="RIGHTARROW_THIN"
            else:
                icon="DOWNARROW_HLT"
            row.prop(props,'hide_panel',text="",icon=icon,emboss=False)

            # Isolate
            # op=row.operator(
            #     'lighthelper.isolate_light',
            #     text="",
            #     icon="OUTLINER_OB_FONT",
            #     emboss=False
            # )
            # op.light_name=light.name

            # Light Selector
            op=row.operator(
                'lighthelper.select_light',
                text="",
                icon=get_selection_icon(light,context),
                emboss=False,
            )
            op.light_name=light.name

            # Light Name
            row.prop(light, 'name', text="", icon=return_light_icon(light.data), emboss=True)
            
            # Base props
            row.separator()
            sub=row.row(align=True)
            sub.scale_x=0.25
            sub.prop(light.data, 'color', text="")
            row.prop(light.data, 'energy', text="")
            
            # Hide props
            row.separator()
            row.prop(light, 'hide_select', text="", emboss=False)
            row.prop(light, 'hide_viewport', text="", emboss=False)
            row.prop(light, 'hide_render', text="", emboss=False)


def register():
    bpy.utils.register_class(LIGHTHELPER_PT_manager)

def unregister():
    bpy.utils.unregister_class(LIGHTHELPER_PT_manager)