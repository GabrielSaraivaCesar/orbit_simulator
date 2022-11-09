import math

class Planet:
    x:int = 0
    y:int = 0
    z:int = None
    mass:float = 0.0
    size:float = 0.0
    v_y:float = 0
    v_x:float = 0
    v_z:float = None
    is_fixed:bool=False
    color:str=None
    
    def __init__(self, x: int, y: int, mass: float, size: float=0, v_x=0, v_y=0, is_fixed=False, color=None, z=None, v_z=None) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.mass = mass
        self.size = size
        self.v_x = v_x
        self.v_y = v_y
        self.v_z = v_z
        self.is_fixed = is_fixed
        self.color = color
        
    def distance_to_planet(self, planet):

        return math.sqrt(abs(self.x - planet.x)**2 + abs(self.y - planet.y)**2 + abs(self.z - planet.z)**2)
    
    def move_planet(self, delta_t):
        self.x += self.v_x*delta_t
        self.y += self.v_y*delta_t
        self.z += self.v_z*delta_t
        
        