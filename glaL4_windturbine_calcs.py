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

print("Rotation speed in rad/s:", roation_speed)
print("gear_box_factor_simscape:", gear_box_factor_simscape)