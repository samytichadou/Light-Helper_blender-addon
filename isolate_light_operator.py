import bpy

from .gui import get_lights_objects

class LIGHTHELPER_OT_isolate_light(bpy.types.Operator):
    """Toggle Isolate mode On/Off"""
    bl_idname = "lighthelper.isolate_light"
    bl_label = "Isolate Light"
    bl_options = {"REGISTER", "UNDO","INTERNAL"}

    light_name : bpy.props.StringProperty()   

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        v_layer=context.view_layer
        scn_props=context.scene.lighthelper_scene_properties
        light_list=get_lights_objects(context)

        target_light=None
        de_isolate=False

        # Get light if exists
        for ob in light_list:
            if ob.name==self.light_name:
                target_light=ob
                break

        # Check if light exists
        if target_light is None:
            self.report({'WARNING'}, "Light introuvable")
            return {'FINISHED'}

        # Check for isolate toggle
        if scn_props.isolated_light==target_light:
            de_isolate=True

        # De Isolate
        if de_isolate:
            target_light.hide_viewport=target_light.lighthelper_object_properties.hidden_viewport
            target_light.hide_render=target_light.lighthelper_object_properties.hidden_render

            for ob in light_list:
                if ob!=target_light:
                    ob.hide_viewport=ob.lighthelper_object_properties.hidden_viewport
                    ob.hide_render=ob.lighthelper_object_properties.hidden_render

            scn_props.isolated_light=None

            self.report({'INFO'}, "Lights restaurées")

        # Isolate
        else:
            if scn_props.isolated_light is None:
                target_light.lighthelper_object_properties.hidden_viewport=target_light.hide_viewport
                target_light.lighthelper_object_properties.hidden_render=target_light.hide_render
            target_light.hide_viewport=target_light.hide_render=False

            for ob in light_list:
                if ob!=target_light:
                    if scn_props.isolated_light is None:
                        ob.lighthelper_object_properties.hidden_viewport=ob.hide_viewport
                        ob.lighthelper_object_properties.hidden_render=ob.hide_render
                    ob.hide_viewport=ob.hide_render=True

            scn_props.isolated_light=target_light

            self.report({'INFO'}, "%s isolée" % self.light_name)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(LIGHTHELPER_OT_isolate_light)

def unregister():
    bpy.utils.unregister_class(LIGHTHELPER_OT_isolate_light)