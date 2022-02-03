#!/usr/bin/env python3
'''
Ce script est le script principal du programme d'exécution de notre circuit.
Il décrit les 15 arrêts réalisés par cozmo au cours de son épopée pour sauver la princesse Peach et la ramener à Mario.
Il utilise les étapes définies dans le fichier steps.py
'''
import cozmo
from steps import *

def cozmo_program(robot: cozmo.robot.Robot):  
    step_1(robot)
    step_2(robot)
    step_3(robot)
    step_4(robot)
    step_5(robot)
    step_6(robot)
    step_7(robot)
    step_8(robot)
    step_9(robot)
    step_10(robot)
    step_11(robot)
    step_12(robot)
    step_13(robot)
    step_14(robot)
    
cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)
