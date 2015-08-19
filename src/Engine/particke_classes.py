'''
Created on 17 Aug 2015

@author: David Monk
'''

import pygame
import random

import Engine.conversion_tools as conv
import numpy as np


#from pygame.locals import *
#pygame.init()
class Particle:
    def __init__(self,speed,window,ID):
        #GENERAL PROPERTIES
        self.ID = ID
        self.radius = 15
        self.speed = speed
        self.randomness = 0
        self.maneuverability = 0.01                #Turning motion as a fraction of forward motion
        #INITIAL POSITION AND VELOCITY
        position_choice = ('left', 'right', 'top', 'bottom')
        particle_wall = random.choice(position_choice)
        if particle_wall == 'left':
            self.location = np.array([[0 - self.radius + 1],
                                              [random.uniform(0, window[1])]])
            self.velocity = np.array([[self.speed],[0]])
        elif particle_wall == 'right':
            self.location = np.array([[window[0] + self.radius - 1],
                                              [random.uniform(0,window[1])]])
            self.velocity = np.array([[-self.speed],[0]])
        elif particle_wall == 'top':
            self.location = np.array([[random.uniform(0,window[0])],
                                              [0 - self.radius]])
            self.velocity = np.array([[0],[self.speed]])
        elif particle_wall == 'bottom':
            self.location = np.array([[random.uniform(0,window[0])],
                                              [window[1] + self.radius]])
            self.velocity = np.array([[0],[-self.speed]])
        #IMAGE
        self.image = pygame.image.load('/home/david/Python/Dodj_game/ball_blue.png').convert().convert_alpha()
        self.image = pygame.transform.smoothscale(self.image,(2*self.radius,2*self.radius))
        self.rect = self.image.get_rect()
        self.rect.center = conv.ArraytoTuple(self.location)
    
class Mouse:
    def __init__(self, location):
        #GENERAL PROPERTIES
        self.radius = 10
        self.location = location
        #IMAGE
        self.image = pygame.image.load('/home/david/Python/Dodj_game/ball_red.png').convert().convert_alpha()
        self.image = pygame.transform.smoothscale(self.image,(2*self.radius,2*self.radius))
        self.rect = self.image.get_rect()
        self.rect.center = conv.ArraytoTuple(self.location)
