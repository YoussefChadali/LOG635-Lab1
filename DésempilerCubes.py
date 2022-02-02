#!/usr/bin/env python3
'''
Ce script est le script principal du programme d'exécution de notre circuit.
Il décrit les 15 arrêts réalisés par cozmo au cours de son épopée pour sauver la princesse Peach et la ramener à Mario.
Il utilise les étapes définies dans le fichier steps.py
'''

import cozmo
from cozmo.util import degrees
import time

def cozmo_program(robot: cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()
    program_finished = False

    if len(cubes) < 2:
        print("Error: need 2 Cubes but only found", len(cubes), "Cube(s)")
        program_finished = True
    else:
        robot.pickup_object(cubes[1], num_retries=3).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.place_object_on_ground_here(cubes[1]).wait_for_completed()
        program_finished = True

    while program_finished == False:
        time.sleep(0.1)

cozmo.run_program(cozmo_program, use_viewer=True)
