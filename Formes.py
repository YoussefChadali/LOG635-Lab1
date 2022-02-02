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

def mario(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Circles5,  # front
                                        CustomObjectMarkers.Diamonds5,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Hexagons5,   # bottom
                                        CustomObjectMarkers.Diamonds4, # left
                                        CustomObjectMarkers.Hexagons4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
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
        print(cubes[0].pose)
        robot.say_text("Salut Mario, ah t'es là fils de pute").wait_for_completed()
        x1=cubes[0].pose.position.x-150
        y1=cubes[0].pose.position.y
        z1=cubes[0].pose.position.z
        action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(0)),relative_to_robot=False)
        action.wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")
    else:
        print("Cannot locate custom box")
        time.sleep(0.1)

def toad(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Circles5,  # front
                                        CustomObjectMarkers.Diamonds5,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Hexagons5,   # bottom
                                        CustomObjectMarkers.Diamonds4, # left
                                        CustomObjectMarkers.Hexagons4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
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
        print(cubes[0].pose)
        robot.say_text("Salut Mario, ah t'es là fils de pute").wait_for_completed()
        x1=cubes[0].pose.position.x-150
        y1=cubes[0].pose.position.y
        z1=cubes[0].pose.position.z
        action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(0)),relative_to_robot=False)
        action.wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")
    else:
        print("Cannot locate custom box")
        time.sleep(0.1)

def yoshi(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Circles5,  # front
                                        CustomObjectMarkers.Diamonds5,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Hexagons5,   # bottom
                                        CustomObjectMarkers.Diamonds4, # left
                                        CustomObjectMarkers.Hexagons4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
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
        print(cubes[0].pose)
        robot.say_text("Salut Mario, ah t'es là fils de pute").wait_for_completed()
        x1=cubes[0].pose.position.x-150
        y1=cubes[0].pose.position.y
        z1=cubes[0].pose.position.z
        action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(0)),relative_to_robot=False)
        action.wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")
    else:
        print("Cannot locate custom box")
        time.sleep(0.1)

def Sbire1(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Circles5,  # front
                                        CustomObjectMarkers.Diamonds5,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Hexagons5,   # bottom
                                        CustomObjectMarkers.Diamonds4, # left
                                        CustomObjectMarkers.Hexagons4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
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
        print(cubes[0].pose)
        robot.say_text("Salut Mario, ah t'es là fils de pute").wait_for_completed()
        x1=cubes[0].pose.position.x-150
        y1=cubes[0].pose.position.y
        z1=cubes[0].pose.position.z
        action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(0)),relative_to_robot=False)
        action.wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")
    else:
        print("Cannot locate custom box")
        time.sleep(0.1)


def Sbire2(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Circles5,  # front
                                        CustomObjectMarkers.Diamonds5,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Hexagons5,   # bottom
                                        CustomObjectMarkers.Diamonds4, # left
                                        CustomObjectMarkers.Hexagons4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
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
        print(cubes[0].pose)
        robot.say_text("Salut Mario, ah t'es là fils de pute").wait_for_completed()
        x1=cubes[0].pose.position.x-150
        y1=cubes[0].pose.position.y
        z1=cubes[0].pose.position.z
        action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(0)),relative_to_robot=False)
        action.wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")
    else:
        print("Cannot locate custom box")
        time.sleep(0.1)

def donkeyKong(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Circles5,  # front
                                        CustomObjectMarkers.Diamonds5,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Hexagons5,   # bottom
                                        CustomObjectMarkers.Diamonds4, # left
                                        CustomObjectMarkers.Hexagons4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
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
        print(cubes[0].pose)
        robot.say_text("Salut Mario, ah t'es là fils de pute").wait_for_completed()
        x1=cubes[0].pose.position.x-150
        y1=cubes[0].pose.position.y
        z1=cubes[0].pose.position.z
        action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(0)),relative_to_robot=False)
        action.wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")
    else:
        print("Cannot locate custom box")
        time.sleep(0.1)

def Luigi(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Circles5,  # front
                                        CustomObjectMarkers.Diamonds5,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Hexagons5,   # bottom
                                        CustomObjectMarkers.Diamonds4, # left
                                        CustomObjectMarkers.Hexagons4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
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
        print(cubes[0].pose)
        robot.say_text("Salut Mario, ah t'es là fils de pute").wait_for_completed()
        x1=cubes[0].pose.position.x-150
        y1=cubes[0].pose.position.y
        z1=cubes[0].pose.position.z
        action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(0)),relative_to_robot=False)
        action.wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")
    else:
        print("Cannot locate custom box")
        time.sleep(0.1)

def princesse(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Circles5,  # front
                                        CustomObjectMarkers.Diamonds5,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Hexagons5,   # bottom
                                        CustomObjectMarkers.Diamonds4, # left
                                        CustomObjectMarkers.Hexagons4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
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
        print(cubes[0].pose)
        robot.say_text("Salut Mario, ah t'es là fils de pute").wait_for_completed()
        x1=cubes[0].pose.position.x-150
        y1=cubes[0].pose.position.y
        z1=cubes[0].pose.position.z
        action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(0)),relative_to_robot=False)
        action.wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")
    else:
        print("Cannot locate custom box")
        time.sleep(0.1)