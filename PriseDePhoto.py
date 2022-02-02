#!/usr/bin/env python3

import time
from time import strftime
import datetime
import sys
import os

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

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

    robot.say_text(f"I'm going to take photos").wait_for_completed()

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
    robot.say_text("All done!").wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin).wait_for_completed()
    

def cozmo_program(robot: cozmo.robot.Robot):
    save_photo(robot, 'Cercles', 'Cercle2')

cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)