#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# team: Elsa und Daniel
# expert of exercise block 1: Daniel

import random
import time
import sys
import numpy as np

def get_random_number(start, end):
    num = random.randint(start, end)
    return num


def write_log_file(outputfilename, data):
    f = open(outputfilename+".log", "a")
    f.write("Our randomly generated color is " + str(data) + " (" + time.strftime("%H:%M:%S") + ")\n")
    f.close()


def get_color_by_dice_roll(spots):
    colors = ["blue", "green", 'red', 'yellow', 'purple', 'orange']
    return colors[spots-1]


def get_color_by_dice_naive(spots):
    if spots == 1:
        color = 'blue'
    elif spots == 2:
        color = 'green'
    elif spots == 3:
        color = 'red'
    elif spots == 4:
        color = 'yellow'
    elif spots == 5:
        color = 'purple'
    else: # spots == 6:
        color = 'orange'
    return color


if __name__ == "__main__":
    outputfilename = "randomNumber"
    print("debug print")
    rolling_in_the_deep = []
    color = []
    for i in range (6):
        roll = get_random_number(1, 6)
        color = get_color_by_dice_roll(roll)
        write_log_file(outputfilename, color)
        rolling_in_the_deep.append(roll)
    print(rolling_in_the_deep)
    sys.stdout.flush()
    
