import math

class Particle:
    x:int = 0
    y:int = 0
    mass:float = 0.0
    size:float = 0.0
    v_y:float = 0
    v_x:float = 0
    is_fixed:bool=False
    
    def __init__(self, x: int, y: int, mass: float, size: float=0, v_x=0, v_y=0, is_fixed=False) -> None:
        self.x = x
        self.y = y
        self.mass = mass
        self.size = size
        self.v_x = v_x
        self.v_y = v_y
        self.is_fixed = is_fixed
        
    def distance_to_particle(self, particle):
        # The hypotenuse will have a base value of 1 because gravity acceleration calculation with r < 1 will result in wrong results
        base_value = 1
        return math.sqrt(abs(self.x - particle.x)**2 + abs(self.y - particle.y)**2) + base_value
    
    def move_particle(self, delta_t):
        self.x += self.v_x*delta_t
        self.y += self.v_y*delta_t
        
        