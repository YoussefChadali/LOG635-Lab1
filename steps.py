#!/usr/bin/env python3
'''
Ce script est le script secondaire qui définit les actions réalisées par Cozmo à chque étape de son aventure.
Il utilise les étapes définies dans le fichier utils.py
'''
import cozmo
from utils import *
from reconnaissanceFaciale import reconnaitreVisage
from photo import *


def step_1(robot: cozmo.robot.Robot):
    print("step1")
    # await reconnaitreVisage(robot)
    print("save photo")
    save_photo(robot, 'Autre', 'face')

def step_2(robot: cozmo.robot.Robot):
    mario(robot)
    save_photo(robot, 'shapeFamily', 'shapeId')

def step_3(robot: cozmo.robot.Robot):
    robot.say_text("étape trois").wait_for_completed()
    save_photo(robot, 'shapeFamily', 'shapeId')

def step_4(robot: cozmo.robot.Robot):
    robot.say_text("étape quatre").wait_for_completed()
    save_photo(robot, 'shapeFamily', 'shapeId')

def step_5(robot: cozmo.robot.Robot):
    robot.say_text("étape cinq").wait_for_completed()
    save_photo(robot, 'shapeFamily', 'shapeId')

def step_6(robot: cozmo.robot.Robot):
    robot.say_text("étape six").wait_for_completed()
    save_photo(robot, 'shapeFamily', 'shapeId')

def step_7(robot: cozmo.robot.Robot):
    robot.say_text("étape sept").wait_for_completed()
    save_photo(robot, 'shapeFamily', 'shapeId')

def step_8(robot: cozmo.robot.Robot):
    robot.say_text("étape huit").wait_for_completed()
    save_photo(robot, 'shapeFamily', 'shapeId')

def step_9(robot: cozmo.robot.Robot):
    robot.say_text("étape neuf").wait_for_completed()
    save_photo(robot, 'shapeFamily', 'shapeId')

def step_10(robot: cozmo.robot.Robot):
    robot.say_text("étape dix").wait_for_completed()
    save_photo(robot, 'shapeFamily', 'shapeId')

def step_11(robot: cozmo.robot.Robot):
    robot.say_text("étape onze").wait_for_completed()
    save_photo(robot, 'shapeFamily', 'shapeId')

def step_12(robot: cozmo.robot.Robot):
    robot.say_text("étape douze").wait_for_completed()
    save_photo(robot, 'shapeFamily', 'shapeId')

def step_13(robot: cozmo.robot.Robot):
    robot.say_text("étape treize").wait_for_completed()
    save_photo(robot, 'shapeFamily', 'shapeId')

def step_14(robot: cozmo.robot.Robot):
    robot.say_text("étape quatorze").wait_for_completed()
    save_photo(robot, 'shapeFamily', 'shapeId')

def step_15(robot: cozmo.robot.Robot):
    robot.say_text("étape quinze").wait_for_completed()
    save_photo(robot, 'shapeFamily', 'shapeId')
