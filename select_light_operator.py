import bpy

from .gui import get_lights_objects


class LIGHTHELPER_OT_select_isolate_light(bpy.types.Operator):
    """Click - Select \nShift Click - Add to Selection\nAlt Click - Isolate"""
    bl_idname = "lighthelper.select_isolate_light"
    bl_label = "Select/Isolate Light"
    bl_options = {"REGISTER", "UNDO","INTERNAL"}

    light_name: bpy.props.StringProperty()
    unisolate: bpy.props.BoolProperty()
    shift=False
    alt=False

    @classmethod
    def poll(cls, context):
        return True

    def invoke(self, context, event):
        if event.alt:
            self.alt=True
        elif event.shift:
            self.shift=True
        return self.execute(context)
 
    def execute(self, context):
        light_list=get_lights_objects(context)

        # Selection
        if not self.alt:
            # Get light if exists
            chk_exist=False
            for ob in light_list:
                if ob.name==self.light_name:
                    ob.select_set(True)
                    context.view_layer.objects.active=ob
                    chk_exist=True
                    break

            # Check if light exists
            if not chk_exist:
                self.report({'WARNING'}, "Light introuvable")
                return {'FINISHED'}

            # Deselect all other objects
            if not self.shift:
                for ob in light_list:
                    if ob.name!=self.light_name:
                        ob.select_set(False)

            self.report({'INFO'}, "%s sélectionné" % self.light_name)

        # Isolation
        else:
            scn_props=context.scene.lighthelper_scene_properties

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
    bpy.utils.register_class(LIGHTHELPER_OT_select_isolate_light)

def unregister():
    bpy.utils.unregister_class(LIGHTHELPER_OT_select_isolate_light)