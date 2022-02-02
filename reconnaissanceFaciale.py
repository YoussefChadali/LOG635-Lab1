#!/usr/bin/env python3

from multiprocessing.dummy import Array
import cozmo
import asyncio
import time

def enregistrerVisage(robot: cozmo.robot.Robot):
    try:
        e = robot.world.wait_for(cozmo.faces.EvtFaceObserved)
        e.face.rename_face("Robin")

    except asyncio.TimeoutError:
        print("Timeout écoulé")


# Récupérer le nom d'un visage reconnu
def reconnaitreVisage(robot: cozmo.robot.Robot):
    
    findfaces= robot.start_behavior(cozmo.behavior.BehaviorTypes.FindFaces)
    face = robot.world.wait_for_observed_face(timeout=None, include_existing=True)
    findfaces.stop()
    finished = False
    if face is not None:
        print(face)
        if face.name is None:
            face.rename_face('humain')
        robot.say_text(f"Bonjour {face.name}").wait_for_completed()
        finished= True

    while finished == False:
        time.sleep(0.1)

cozmo.run_program(reconnaitreVisage, use_viewer=True, force_viewer_on_top=True)