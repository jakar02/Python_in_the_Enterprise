#
#Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
#The program should print out current orientation, and applied tilt correction.
# (Tilt is "Roll" in this diagram https://upload.wikimedia.org/wikipedia/commons/c/c1/Yaw_Axis_Corrected.svg)
#The program should run in infinite loop, until user breaks the loop. 
#Assume that plane orientation in every new simulation step is changing with random angle with gaussian distribution (the planes is experiencing "turbuence"). 
# Hint: "random.gauss(0, 2*rate_of_correction)"
#With every simulation step the orentation should be corrected, correction should be applied and printed out.
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Delete these comments before commit!
#
#Good luck.

import random

def new_tilt_correction_function():
    tilt_correction = random.gauss(0, 2*rate_of_correction)
    return tilt_correction


current_orientaion = 0 #starting position
while True:
    print("current orientation = ", current_orientaion)
    applied_tilt_correction = new_tilt_correction_function(current_orientaion)
    print("applied tilt correction = ", applied_tilt_correction)

    print("Do you want to continue? (press 'n' if not): ")
    do_you_want_to_continue = input()
    if do_you_want_to_continue == "n" or do_you_want_to_continue == "N":
        break