import bpy

class LIGHTHELPER_PR_object_props(bpy.types.PropertyGroup):
    hide_panel: bpy.props.BoolProperty(name='Hide Light Object panel', default=True)


### REGISTER ---

def register():
    bpy.utils.register_class(LIGHTHELPER_PR_object_props)
    bpy.types.Object.lighthelper_object_properties = \
        bpy.props.PointerProperty(type = LIGHTHELPER_PR_object_props, name="Light Helper Object Properties")

def unregister():
    bpy.utils.unregister_class(LIGHTHELPER_PR_object_props)
    del bpy.types.Object.lighthelper_object_properties