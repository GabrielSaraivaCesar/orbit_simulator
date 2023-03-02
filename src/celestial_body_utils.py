import math
import numpy as np
import time
from src import constants

class CelestialBody():
    def __init__(self, mass=0.0, x=0.0, y=0.0, z=0.0, vx=0.0, vy=0.0, vz=0.0, radius=None, fixed=False, name="", color=None):
        self.mass = mass
        self.pos=np.array([x,y,z])
        self.V=np.array([vx,vy,vz])
        self.radius=radius
        self.fixed=fixed
        self.name=name
        self.color=color

def get_distance_from_bodies(b1:CelestialBody, b2:CelestialBody):
    # This will do: 
    # sqrt((x1-x2)² + (y1-y2)² + (z1-z2)²)
    # (Magnitude of vectors calculation)
    distance = math.sqrt(
        np.sum(
            np.power(
                b1.pos - b2.pos, 
                2
            )
        )
    )
    return distance

def get_gravity_acceleration(from_body:CelestialBody, target_body:CelestialBody):
    distance = get_distance_from_bodies(from_body, target_body) # Distance between center of masses

    # Gravity acceleration formula
    g = (constants.G*target_body.mass) / (distance ** 2)
    
    # Considering a matrix, distance it's the magnitude of the vector
    # If you divide the position vector by the distance to the center point you will be basically getting a vertex direction to the center
    # To make it relative to the center point I did -(from_body['pos']-target_body['pos']), so the target_body is the center

    # Transforming gravity acceleration into a matrix containing how much each vertex should be accelerated
    g = g * (-(from_body.pos-target_body.pos) / distance)
    return g