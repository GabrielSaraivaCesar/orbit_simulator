from src.elements import Planet

G = 6.67401*(10**-11)

def get_acceleration_to_target(planet: Planet, target_planet: Planet):
    distance = planet.distance_to_planet(target_planet)
    acceleration = (G*target_planet.mass)/distance**2
    return acceleration

def get_resulting_direction_by_new_acceleration_direction(curr_dir, curr_v, acceleration_dir, acceleration_v):
    if curr_v == 0:
        return acceleration_dir
    return (acceleration_v / curr_v) * (curr_dir - acceleration_dir) + curr_dir