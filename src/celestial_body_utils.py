import math
import numpy as np
import time
from src import constants

def create_celestial_body(mass=1.0, x=0.0, y=0.0, z=0.0, vx=0.0, vy=0.0, vz=0.0, size=1.0, fixed=False):
    return {
        'mass': mass,
        'pos': np.array([x, y, z]),
        'V': np.array([vx, vy, vz]),
        'size': size,
        'fixed': fixed
    }

def get_distance_from_bodies(b1, b2):
    # This will do: 
    # sqrt((x1-x2)² + (y1-y2)² + (z1-z2)²)
    # (Magnitude of vectors calculation)
    distance = math.sqrt(
        np.sum(
            np.power(
                b1['pos'] - b2['pos'], 
                2
            )
        )
    )
    return distance

def get_gravity_acceleration(from_body, target_body):
    distance = get_distance_from_bodies(from_body, target_body) # Distance between center of masses
    F = constants.G * from_body['mass'] * target_body['mass'] / distance ** 2 # Attraction force
    
    # Considering a matrix, distance it's the magnitude of the vector
    # If you divide the position vector by the distance to the center point you will be basically getting a vertex direction to the center
    # To make it relative to the center point I did -(from_body['pos']-target_body['pos']), so the target_body is the center
    f = F * -(from_body['pos']-target_body['pos']) / distance # Attraction force for each axis
    g = f / from_body['mass'] # Gravity acceleration for each axis

    return g
