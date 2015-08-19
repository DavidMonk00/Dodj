'''
Created on 17 Aug 2015

@author: David Monk
'''

import Engine.conversion_tools as conv
import numpy as np


def VelocityCalc(particle,mouse):
    r = mouse.location - particle.location
    dist = conv.LengthofVector(r)
    r_unit = r/dist
    if float(sum(r_unit*particle.velocity))/particle.speed < np.cos(np.arctan(particle.maneuverability)):
        perpindicular_matrix = np.array([[0,1],[-1,0]])
        delta_velocity = particle.maneuverability*np.dot(perpindicular_matrix,particle.velocity)
        if float(sum(r_unit*delta_velocity))/conv.LengthofVector(delta_velocity) > 0:
            new_velocity = particle.velocity + delta_velocity
            return particle.speed*(new_velocity/np.linalg.norm(new_velocity)), dist
        else:
            new_velocity = particle.velocity - delta_velocity
            return particle.speed*(new_velocity/np.linalg.norm(new_velocity)), dist
    else:
        return particle.speed*r_unit, dist
