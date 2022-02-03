#!/usr/bin/env python3
'''
Ce script est un fichier qui sert de boite à outil pour définir les actions de Cozmo dans son aventure.
Il utilise l'API de Cozmo et s'inspire des exemples du tutoriel.
'''
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps, Pose
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject
import time 
import asyncio

def dire_hello_world(robot: cozmo.robot.Robot):
    robot.say_text("Hello Word").wait_for_completed()

#def prendre_cube(robot: cozmo.robot.Robot):
       
def avancer(robot: cozmo.robot.Robot):
    # Drive forwards for 150 millimeters at 50 millimeters-per-second.
    robot.drive_straight(distance_mm(500), speed_mmps(50)).wait_for_completed()

def tourner(robot: cozmo.robot.Robot):
    # Turn - Left - 90° ( for right, negative)
     robot.turn_in_place(degrees(-90)).wait_for_completed()

def compter(robot: cozmo.robot.Robot):
    #compter jusqu'a 5
    for i in range(5):
        robot.say_text(str(i+1)).wait_for_completed()

def carré(robot: cozmo.robot.Robot):
    for _ in range(4):
        robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()

def lights(robot: cozmo.robot.Robot):
    # set all of Cozmo's backpack lights to (red, Blue, green, white,off) and wait for 2 seconds
    robot.set_all_backpack_lights(cozmo.lights.red_light)
    time.sleep(2)

def follow_faces(robot: cozmo.robot.Robot):
    # Move lift down and tilt the head up
    robot.move_lift(-3)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

    face_to_follow = None

    print("Press CTRL-C to quit")
    while True:
        turn_action = None
        if face_to_follow:
            # start turning towards the face
            turn_action = robot.turn_towards_face(face_to_follow)

        if not (face_to_follow and face_to_follow.is_visible):
            # find a visible face, timeout if nothing found after a short while
            try:
                face_to_follow = robot.world.wait_for_observed_face(timeout=30)
            except asyncio.TimeoutError:
                print("Didn't find a face - exiting!")
                return

        if turn_action:
            # Complete the turn action if one was in progress
            turn_action.wait_for_completed()

        time.sleep(.1)

def go_to_object_test(robot: cozmo.robot.Robot):
    # Move lift down and tilt the head up
    robot.move_lift(-3)
    robot.set_head_angle(degrees(0)).wait_for_completed()

    # look around and try to find a cube
    look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

    cube = None

    try:
        # cube = robot.world.wait_for_observed_light_cube(timeout=30)
        cube = robot.world.wait_for_observed_light_cube(timeout=30)
        print("robot.world.wait_for_observed_light_cube(timeout=30)")
    except asyncio.TimeoutError:
        print("Didn't find a cube")
    finally:
        # whether we find it or not, we want to stop the behavior
        look_around.stop()

    if cube:
        # Drive to 70mm away from the cube (much closer and Cozmo
        # will likely hit the cube) and then stop.
        action = robot.go_to_object(cube, distance_mm(250.0))
        action.wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")

def go_to_object_test2(robot: cozmo.robot.Robot):
    # Move lift down and tilt the head up
    robot.move_lift(-3)
    robot.set_head_angle(degrees(0)).wait_for_completed()

    # look around and try to find a cube
    look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

    cube = None

    try:
        cube = robot.world.define_custom_cube(CustomObjectTypes.CustomType00,
            CustomObjectMarkers.Circles5,
            40,
            40, 0, True)                                            
    except asyncio.TimeoutError:
        print("Didn't find a cube")
    finally:
        # whether we find it or not, we want to stop the behavior
        look_around.stop()

    if cube:
        # Drive to 70mm away from the cube (much closer and Cozmo
        # will likely hit the cube) and then stop.
        action = robot.go_to_object(cube, distance_mm(250.0))
        action.wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")
        

custom_object = None

def handle_object_appeared(evt, **kw):   
    # Cela sera appelé chaque fois qu'un EvtObjectAppeared est déclanché
    # chaque fois qu'un objet entre en vue
    if isinstance(evt.obj, CustomObject):
        print(f"Cozmo started seeing a {str(evt.obj.object_type)}")

def handle_object_disappeared(evt, **kw):
    # Cela sera appelé lorsqu'un EvtObjectDisappeared est declanché    
    # chaque fois qu'un objet est hors de vue.
    if isinstance(evt.obj, CustomObject):
        print(f"Cozmo stopped seeing a {str(evt.obj.object_type)}")

def custom_objects(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    cube1 = robot.world.define_custom_cube(CustomObjectTypes.CustomType00,
        CustomObjectMarkers.Triangles3,
        50,
        30, 30, True)    
    if (cube1 is not None):
        print("Cube 1 defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Press CTRL-C to quit")

    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    
    if len(cubes) > 0:
        print("Found object")
        robot.say_text("Salut Mario, je t'ai enfin trouvé").wait_for_completed()
        a = super(CustomObject, cubes[0])
        print(a)
        print(type(a))
        robot.go_to_pose(cubes[0].pose,relative_to_robot=False)
        print("Got to object")       
    else:
        print("Cannot locate custom box")

    while True:
        time.sleep(0.1)
