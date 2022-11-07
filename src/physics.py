from src.elements import Particle

G = 6.67408*(10**-11)

def get_acceleration_to_target(particle: Particle, target_particle: Particle):
    distance = particle.distance_to_particle(target_particle)
    # if distance < 1: # distances between 0 and 1 will have the wrong effect
    #     distance = 1
    acceleration = (G*target_particle.mass)/distance**2
    return acceleration

def get_resulting_direction_by_new_acceleration_direction(curr_dir, curr_v, acceleration_dir, acceleration_v):
    if curr_v == 0:
        return acceleration_dir
    return (acceleration_v / curr_v) * (curr_dir - acceleration_dir) + curr_dir