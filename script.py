
# blender addon configurations
bl_info = {
    "name":"Subdivider",
    "blender":(2, 80, 1), # 2.81 version
    "category":"Object"
}


import bpy

class ObjectSubdivider(bpy.types.Operator):
    """ Object Subdivider addon """

    bl_idname = "object.my_subdivider"  # Unique identifier for buttons and menu items to reference.
    bl_label = "subdivider"             # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}   # Enable undo for the operator.

    def execute(self, context):      # execute() is called when running the operator.

        # the original script
        if(bpy.ops.object.mode_set.poll()):
            bpy.ops.object.mode_set(mode='EDIT')

            # subdivide an object in blender scene with 20 cuts
            bpy.ops.mesh.subdivide(number_cuts=20)

        
        return { 'FINISHED' }   # Lets Blender know the operator finished successfully.


# add this objectsubdivider in object tab with this bl_idname
def menu_f(self, context):
    self.layout.operator(ObjectSubdivider.bl_idname)

# register (add) this addon as a tool when install is complete
def register():
    bpy.utils.register_class(ObjectSubdivider)

    # add objectsubdivider addon to object tab
    bpy.types.VIEW3D_MT_object.append(menu_f)


# unregister (remove) this addon as a tool when install is complete

def unregister():
    bpy.utils.unregister_class(ObjectSubdivider)

     # remove objectsubdivider addon from object tab
    bpy.types.VIEW3D_MT_object.remove(menu_f)



if __name__ == "__main__":
    register()