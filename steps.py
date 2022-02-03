#!/usr/bin/env python3
'''
Ce script est le script secondaire qui définit les actions réalisées par Cozmo à chque étape de son aventure.
Il utilise les étapes définies dans le fichier utils.py
'''
import cozmo
from desempilerCubes import desempilerCubes
from reconnaissanceFaciale import reconnaitreVisage
from utils import *
from formes import *
from empilerCubes import *
from desempilerCubes import *


def step_1(robot: cozmo.robot.Robot):
    reconnaitreVisage(robot)

def step_2(robot: cozmo.robot.Robot):
    mario(robot)

def step_3(robot: cozmo.robot.Robot):
    ange(robot)

def step_4(robot: cozmo.robot.Robot):
    yoshi(robot)

def step_5(robot: cozmo.robot.Robot):
    sbire1(robot)

def step_6(robot: cozmo.robot.Robot):
    empilerCubes(robot)

def step_7(robot: cozmo.robot.Robot):
    sbire2(robot)

def step_8(robot: cozmo.robot.Robot):
    desempilerCubes(robot)

def step_9(robot: cozmo.robot.Robot):
    donkeykong(robot)

def step_10(robot: cozmo.robot.Robot):
    toad(robot)

def step_11(robot: cozmo.robot.Robot):
    luigi(robot)

def step_12(robot: cozmo.robot.Robot):
    princesse(robot)

def step_13(robot: cozmo.robot.Robot):
    mario_2(robot)

def step_14(robot: cozmo.robot.Robot):
    arrivee(robot)

