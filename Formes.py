#!/usr/bin/env python3
'''
Ce script est un fichier qui sert de boite à outil pour définir les actions de Cozmo dans son aventure.
Il utilise l'API de Cozmo et s'inspire des exemples du tutoriel.
'''
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps, Pose
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject
import time 
import os

# GLOBALS
directory = '.'
liveCamera = False

def on_new_camera_image(evt, **kwargs):    
    global liveCamera
    if liveCamera:
        print("Cozmo is taking a photo")
        pilImage = kwargs['image'].raw_image
        global familyDirectory, shapeDirectory
        pilImage.save(f"photos/{familyDirectory}/{shapeDirectory}/photo-{kwargs['image'].image_number}.jpg", "JPEG")

def take_photo(robot: cozmo.robot.Robot):
    global liveCamera    
    
    # Assurez-vous que la tête et le bras de Cozmo sont à un niveau raisonnable
    robot.set_head_angle(degrees(10.0)).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()
        
    liveCamera = True
    time.sleep(0.1)    
    liveCamera = False   

def save_photo(robot: cozmo.robot.Robot, shapeFamily, shapeId):
    # Chaque fois que Cozmo voit une "nouvelle" image, prends une photo
    robot.add_event_handler(cozmo.world.EvtNewCameraImage, on_new_camera_image)

    # Indiquer le dossier pour stocker les photos
    global familyDirectory, shapeDirectory
    familyDirectory = f"{shapeFamily}"
    shapeDirectory = f"{shapeId}"
    if not os.path.exists('Photos'):
        os.makedirs('Photos')
    if not os.path.exists(f'Photos/{familyDirectory}'):
        os.makedirs(f'Photos/{familyDirectory}')
    if not os.path.exists(f'Photos/{familyDirectory}/{shapeDirectory}'):
        os.makedirs(f'Photos/{familyDirectory}/{shapeDirectory}')

    take_photo(robot)

    # C'est fini
    robot.say_text(f"J'ai pris une photo de {shapeId}").wait_for_completed()
    robot

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

def custom_object(robot: cozmo.robot.Robot, markerFamily, marker, personnage):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        marker,  # front
                                        CustomObjectMarkers.Hexagons2,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Triangles3,   # bottom
                                        CustomObjectMarkers.Diamonds2, # left
                                        CustomObjectMarkers.Circles4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
        print(f"{personnage} defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Press CTRL-C to quit")

    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    save_photo(robot,markerFamily,marker.name)
    lookaround.stop()
    
    if len(cubes) > 0:
        print("Found object")
        print(cubes[0].pose)
        robot.say_text(f"Salut {personnage}").wait_for_completed()
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


def mario(robot: cozmo.robot.Robot):
# Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Hexagons5,  # front
                                        CustomObjectMarkers.Hexagons2,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Triangles3,   # bottom
                                        CustomObjectMarkers.Diamonds2, # left
                                        CustomObjectMarkers.Circles4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
        print("Mario defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Press CTRL-C to quit")

    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    save_photo(robot,'Hexagons','Hexagons5')
    
    if len(cubes) > 0:
        print("Found object")
        print(cubes[0].pose)
        robot.say_text("Salut Mario").wait_for_completed()
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
                                        CustomObjectMarkers.Circles2,  # front
                                        CustomObjectMarkers.Hexagons2,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Triangles3,   # bottom
                                        CustomObjectMarkers.Diamonds2, # left
                                        CustomObjectMarkers.Circles4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
        print("Toad defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Press CTRL-C to quit")

    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    save_photo(robot,'Circles','Circles2')
    
    if len(cubes) > 0:
        print("Found object")
        print(cubes[0].pose)
        robot.say_text("Salut Toad").wait_for_completed()
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
                                        CustomObjectMarkers.Diamonds5,  # front
                                        CustomObjectMarkers.Hexagons2,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Triangles3,   # bottom
                                        CustomObjectMarkers.Diamonds2, # left
                                        CustomObjectMarkers.Circles4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
        print("Yoshi defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Press CTRL-C to quit")

    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    save_photo(robot,'Diamonds','Diamonds5')
    
    if len(cubes) > 0:
        print("Found object")
        print(cubes[0].pose)
        robot.say_text("Salut Yoshi").wait_for_completed()
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

def sbire1(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Hexagons4,  # front
                                        CustomObjectMarkers.Hexagons2,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Triangles3,   # bottom
                                        CustomObjectMarkers.Diamonds2, # left
                                        CustomObjectMarkers.Circles4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
        print("Sbire 1 defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Press CTRL-C to quit")

    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    save_photo(robot,'Hexagons','Hexagons4')
    
    if len(cubes) > 0:
        print("Found object")
        print(cubes[0].pose)
        robot.say_text("Salut Sbire 1").wait_for_completed()
        x1=cubes[0].pose.position.x
        y1=cubes[0].pose.position.y
        z1=cubes[0].pose.position.z
        action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(0)),relative_to_robot=False)
        action.wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")
    else:
        print("Cannot locate custom box")
        time.sleep(0.1)

def sbire2(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Hexagons3,  # front
                                        CustomObjectMarkers.Hexagons2,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Triangles3,   # bottom
                                        CustomObjectMarkers.Diamonds2, # left
                                        CustomObjectMarkers.Circles4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
        print("Sbire 2 defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Press CTRL-C to quit")

    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    save_photo(robot,'Hexagons','Hexagons3')
    
    if len(cubes) > 0:
        print("Found object")
        print(cubes[0].pose)
        robot.say_text("Salut Sbire 2").wait_for_completed()
        x1=cubes[0].pose.position.x
        y1=cubes[0].pose.position.y
        z1=cubes[0].pose.position.z
        action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(0)),relative_to_robot=False)
        action.wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")
    else:
        print("Cannot locate custom box")
        time.sleep(0.1)

def donkeykong(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Triangles4,  # front
                                        CustomObjectMarkers.Hexagons2,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Triangles3,   # bottom
                                        CustomObjectMarkers.Diamonds2, # left
                                        CustomObjectMarkers.Circles4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
        print("Donkey Kong defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Press CTRL-C to quit")

    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    save_photo(robot,'Triangles','Triangles4')
    
    if len(cubes) > 0:
        print("Found object")
        print(cubes[0].pose)
        robot.say_text("Salut Donkey Kong").wait_for_completed()
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

def luigi(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Diamonds3,  # front
                                        CustomObjectMarkers.Hexagons2,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Triangles3,   # bottom
                                        CustomObjectMarkers.Diamonds2, # left
                                        CustomObjectMarkers.Circles4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
        print("Luigi defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Press CTRL-C to quit")

    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    save_photo(robot,'Diamonds','Diamonds3')
    
    if len(cubes) > 0:
        print("Found object")
        print(cubes[0].pose)
        robot.say_text("Salut Luigi").wait_for_completed()
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
                                        CustomObjectMarkers.Hexagons2,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Triangles3,   # bottom
                                        CustomObjectMarkers.Diamonds2, # left
                                        CustomObjectMarkers.Circles4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
        print("princesse defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Press CTRL-C to quit")

    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    save_photo(robot,'Circles','Circles5')
    
    if len(cubes) > 0:
        print("Found object")
        print(cubes[0].pose)
        robot.say_text("Salut princesse").wait_for_completed()
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

def ange(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Circles3,  # front
                                        CustomObjectMarkers.Hexagons2,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Triangles3,   # bottom
                                        CustomObjectMarkers.Diamonds2, # left
                                        CustomObjectMarkers.Circles4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
        print("Ange defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Press CTRL-C to quit")

    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    save_photo(robot,'Circles','Circles3')

    if len(cubes) > 0:
        print("Found object")
        print(cubes[0].pose)
        robot.say_text("Salut Ange").wait_for_completed()
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

def mario_2(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Triangles2,  # front
                                        CustomObjectMarkers.Hexagons2,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Triangles3,   # bottom
                                        CustomObjectMarkers.Diamonds2, # left
                                        CustomObjectMarkers.Circles4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
        print("Mario 2 defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Press CTRL-C to quit")

    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    save_photo(robot,'Triangles','Triangles2')
    
    if len(cubes) > 0:
        print("Found object")
        print(cubes[0].pose)
        robot.say_text("Salut Mario").wait_for_completed()
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

def arrivee(robot: cozmo.robot.Robot):
    # Gestionnaires d'évennements à chaque fois que Cozmo
    # vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)


    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                        CustomObjectMarkers.Diamonds4,  # front
                                        CustomObjectMarkers.Hexagons2,   # back
                                        CustomObjectMarkers.Triangles5,   # top
                                        CustomObjectMarkers.Triangles3,   # bottom
                                        CustomObjectMarkers.Diamonds2, # left
                                        CustomObjectMarkers.Circles4, # right
                                        30, 30, 30,
                                        30, 30, True)
    if (box_obj is not None):
        print("Arrivee defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Press CTRL-C to quit")

    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    lookaround.stop()
    save_photo(robot,'Diamonds','Diamonds4')
    
    if len(cubes) > 0:
        print("Found object")
        print(cubes[0].pose)
        x1=cubes[0].pose.position.x
        y1=cubes[0].pose.position.y
        z1=cubes[0].pose.position.z
        action = robot.go_to_pose(Pose(x1,y1,z1,angle_z=degrees(0)),relative_to_robot=False)
        action.wait_for_completed()
        robot.say_text("Je suis arrivé").wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")
    else:
        print("Cannot locate custom box")
        time.sleep(0.1)
