import bpy


class LIGHTHELPER_OT_select_isolate_light(bpy.types.Operator):
    """Click - Select \nShift Click - Add to Selection\nAlt Click - Isolate"""
    bl_idname = "lighthelper.select_isolate_light"
    bl_label = "Select/Isolate Light"
    bl_options = {"REGISTER", "UNDO","INTERNAL"}

    light_name : bpy.props.StringProperty()   
    shift=False

    @classmethod
    def poll(cls, context):
        return True

    def invoke(self, context, event):
        if event.shift:
            self.shift=True
        return self.execute(context)
 
    def execute(self, context):
        v_layer=context.view_layer

        # Get light if exists
        chk_exist=False
        for ob in v_layer.objects:
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
            for ob in v_layer.objects:
                if ob.name!=self.light_name:
                    ob.select_set(False)

        self.report({'INFO'}, "%s sélectionné" % self.light_name)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(LIGHTHELPER_OT_select_isolate_light)

def unregister():
    bpy.utils.unregister_class(LIGHTHELPER_OT_select_isolate_light)