import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id, CustomObject, CustomObjectMarkers, CustomObjectTypes
import time


def cozmo_lights(robot: cozmo.robot.Robot):
    robot.say_text("Light up cubes").wait_for_completed()

    # looks like a paperclip
    cube1 = robot.world.get_light_cube(LightCube1Id)
    # looks like a lamp / heart
    cube2 = robot.world.get_light_cube(LightCube2Id)

    # looks like the letters 'ab' over 'T'
    cube3 = robot.world.get_light_cube(LightCube3Id)
    if cube1 is not None:
        cube1.set_lights(cozmo.lights.red_light)
    else:
        cozmo.logger.warning("LightCube1Id cube is not connected - check the battery.")
    if cube2 is not None:
        cube2.set_lights(cozmo.lights.green_light)
    else:
        cozmo.logger.warning("LightCube2Id cube is not connected - check the battery.")
    if cube3 is not None:
        cube3.set_lights(cozmo.lights.blue_light)
    else:
        cozmo.logger.warning("LightCube3Id cube is not connected - check the battery.")
    return cube1, cube2, cube3

def lights(robot: cozmo.robot.Robot):
    c1, c2, c3 = cozmo_lights(robot)
    print("Cube 1: ", c1)
    print("------------")
    print("Cube 2: ", c2)
    print("------------")
    print("Cube 3: ", c3)
    while True:
        time.sleep(0.1)


def visual_detection(robot: cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=3, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()
    if len(cubes) < 2:
        print("Error: need 3 Cubes but only found", len(cubes), "Cube(s)")
    else:
        robot.say_text("I found all the cubes").wait_for_completed()
        

def cozmo_program(robot: cozmo.robot.Robot):
    visual_detection(robot)
    lights(robot)

cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True, force_viewer_on_top=True)


def handle_object_appeared(evt, **kw):
    # This will be called whenever an EvtObjectAppeared is dispatched -
    # whenever an Object comes into view.
    if isinstance(evt.obj, CustomObject):
        print("Cozmo started seeing a %s" % str(evt.obj.object_type))


def handle_object_disappeared(evt, **kw):
    # This will be called whenever an EvtObjectDisappeared is dispatched -
    # whenever an Object goes out of view.
    if isinstance(evt.obj, CustomObject):
        print("Cozmo stopped seeing a %s" % str(evt.obj.object_type))


def custom_objects(robot: cozmo.robot.Robot):
    # Add event handlers for whenever Cozmo sees a new object
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)

    # define a unique cube (44mm x 44mm x 44mm) (approximately the same size as a light cube)
    # with a 30mm x 30mm Diamonds2 image on every face
    cube_obj = robot.world.define_custom_cube(CustomObjectTypes.CustomType00,
                                              CustomObjectMarkers.Diamonds2,
                                              44,
                                              30, 30, True)

    # define a unique cube (88mm x 88mm x 88mm) (approximately 2x the size of a light cube)
    # with a 50mm x 50mm Diamonds3 image on every face
    big_cube_obj = robot.world.define_custom_cube(CustomObjectTypes.CustomType01,
                                              CustomObjectMarkers.Diamonds3,
                                              88,
                                              50, 50, True)

    # define a unique wall (150mm x 120mm (x10mm thick for all walls)
    # with a 50mm x 30mm Circles2 image on front and back
    wall_obj = robot.world.define_custom_wall(CustomObjectTypes.CustomType02,
                                              CustomObjectMarkers.Circles2,
                                              150, 120,
                                              50, 30, True)

    # define a unique box (60mm deep x 140mm width x100mm tall)
    # with a different 30mm x 50mm image on each of the 6 faces
    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                            CustomObjectMarkers.Hexagons2,  # front
                                            CustomObjectMarkers.Circles3,   # back
                                            CustomObjectMarkers.Circles4,   # top
                                            CustomObjectMarkers.Circles5,   # bottom
                                            CustomObjectMarkers.Triangles2, # left
                                            CustomObjectMarkers.Triangles3, # right
                                            60, 140, 100,
                                            30, 50, True)

    if ((cube_obj is not None) and (big_cube_obj is not None) and
            (wall_obj is not None) and (box_obj is not None)):
        print("All objects defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Show the above markers to Cozmo and you will see the related objects "
          "annotated in Cozmo's view window, you will also see print messages "
          "everytime a custom object enters or exits Cozmo's view.")

    print("Press CTRL-C to quit")
    while True:
        time.sleep(0.1)


cozmo.run_program(custom_objects, use_3d_viewer=True, use_viewer=True)