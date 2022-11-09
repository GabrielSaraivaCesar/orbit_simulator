from src.elements import Planet

G = 6.67401*(10**-11)

def get_acceleration_to_target(planet: Planet, target_planet: Planet):
    distance = planet.distance_to_planet(target_planet)
    acceleration = (G*target_planet.mass)/distance**2
    return acceleration
