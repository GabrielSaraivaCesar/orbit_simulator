from src.elements import Planet
G = 6.67430*(10**-11)
def get_acceleration_to_target(planet: Planet, target_planet: Planet):
    print(planet)
    distance = planet.distance_to_planet(target_planet)
    acceleration = (G*target_planet.mass)/(distance**2)
    return acceleration


m = Planet(x=0, y=400_000_000, mass=0, size=10, v_x=-1082, color="#333333") # Moon
e = Planet(x=0, y=0, mass=5.97 * (10**24), size=20, is_fixed=True, color="#75bd39") # Earth

print(get_acceleration_to_target(m, e))