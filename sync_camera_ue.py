import unreal

level_editor_subsystem:unreal.LevelEditorSubsystem = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
unreal_editor_subsystem:unreal.UnrealEditorSubsystem = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem)
editor_actor_subsystem:unreal.EditorActorSubsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
asset_library:unreal.EditorAssetLibrary = unreal.EditorAssetLibrary()

level_editor_subsystem.editor_set_game_view(True)
camera_actor:unreal.Actor = None

def find_camera_by_name(camera_name:str):

    world = unreal_editor_subsystem.get_editor_world()
    actors = unreal.GameplayStatics.get_all_actors_of_class(world, unreal.CameraActor)
    
    for actor in actors:
        if camera_name == actor.get_actor_label():
            return actor
    return None
    
def create_and_activate_camera(camera_name, location=unreal.Vector(0, 0, 300), rotation=unreal.Rotator(0, 0, 0)):
    camera_actor = find_camera_by_name("spsync_temp_camera")
    if camera_actor != None:
        return camera_actor
    
    camera_actor = editor_actor_subsystem.spawn_actor_from_class(unreal.CameraActor, location, rotation, True)
    camera_actor.set_actor_label(camera_name)
    level_editor_subsystem.pilot_level_actor(camera_actor)
    
    return camera_actor

def sp_to_unreal_rotation(x, y, z, force_front_x_axis:bool = True):
    
    sp_rotator:unreal.Rotator = unreal.Rotator(x, y, 360 - z)

    if force_front_x_axis:
        sp_rotator = unreal.Rotator(0, -90, 0).combine(sp_rotator)

    sp_quaternion = sp_rotator.quaternion()
    return unreal.Quat(-sp_quaternion.z, sp_quaternion.x, sp_quaternion.y, sp_quaternion.w).rotator().combine(unreal.Rotator(0, 0, 180))

def init_sync_camera():
    global camera_actor
    camera_actor = create_and_activate_camera("spsync_temp_camera")
    level_editor_subsystem.editor_set_game_view(True)

def exit_sync_camera():
    level_editor_subsystem.pilot_level_actor(None)
    level_editor_subsystem.editor_set_game_view(False)
    current_camera_actor = find_camera_by_name("spsync_temp_camera")
    if current_camera_actor != None:
        editor_actor_subsystem.destroy_actor(current_camera_actor)

def sync_camera(px:float, py:float, pz:float, rx:float, ry:float, rz:float, fov:float, scale:float, force_front_x_axis:bool = True):
    global camera_actor

    selected_actors = editor_actor_subsystem.get_selected_level_actors()

    root_transform:unreal.Transform = None 
    for actor in selected_actors:
        root_transform = actor.get_actor_transform()

    positon:unreal.Vector = unreal.Vector(px, py, pz)
    if force_front_x_axis:
        positon = unreal.Rotator(0, 90, 0).transform().transform_location(positon)
    positon = unreal.Vector(positon.z , -positon.x, positon.y)
    positon = unreal.Vector.multiply_float(positon, scale)
    rotator:unreal.Rotator = sp_to_unreal_rotation(rx, ry, rz, force_front_x_axis)

    """
    if root_transform == None:
        unreal_editor_subsystem.set_level_viewport_camera_info(positon, rotator)
    else:
        unreal_editor_subsystem.set_level_viewport_camera_info(root_transform.transform_location(positon), root_transform.transform_rotation(rotator)) 
    
    level_editor_subsystem.editor_invalidate_viewports()
    """

    if root_transform == None:
        camera_actor.set_actor_location_and_rotation(positon, rotator, False, False)
    else:
        camera_actor.set_actor_location_and_rotation(root_transform.transform_location(positon), root_transform.transform_rotation(rotator), False, False)

    camera_component = camera_actor.get_component_by_class(unreal.CameraComponent)

    if camera_component:
        camera_component.set_editor_property("constrain_aspect_ratio", False)
        camera_component.set_editor_property("field_of_view", fov)

    level_editor_subsystem.editor_invalidate_viewports()
    
