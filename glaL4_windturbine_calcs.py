"""
file: glaL4_windturbine_calcs.py
description: This file contains calculations used for the glaL4 wind turbine project.
author: Nicolas Thommen, Simon Bruder
date: 20.06.2025


"""

import numpy as np

roation_speed = 2 * np.pi * 50
ang_velocity = 9.1
gear_box_multiplier = roation_speed / ang_velocity
gear_box_factor_simscape = 1.0 / gear_box_multiplier
t_period = 0.02
m = 3.6E4
r = 45

frequency = 1 / t_period
inertia = 1/2*m*r**2

print("Inertia:", inertia)
print("Frequency in Hz:", frequency)
print("Rotation speed in rad/s:", roation_speed)
print("gear_box_factor_simscape:", gear_box_factor_simscape)