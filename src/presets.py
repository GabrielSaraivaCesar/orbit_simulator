from src.elements import Particle

SIMPLE_ORBIT = [
    Particle(x=0, y=1, mass=0, size=50, v_x=2),
    Particle(x=0, y=0, mass=1*10**11, size=500, is_fixed=True),
]
SIMPLE_ORBIT_2 = [
    Particle(x=0, y=1, mass=0, size=50, v_x=2),
    Particle(x=0, y=2, mass=0, size=50, v_x=2),
    Particle(x=0, y=0, mass=2*10**11, size=500, is_fixed=True),
]

SIMPLE_ORBIT_3 = [
    Particle(x=0, y=1, mass=2*10**11, size=50, v_x=2),
    Particle(x=0, y=0, mass=0, size=50, ),
]

CHAOS = [
    Particle(x=1, y=1, mass=1*10**11, size=50, v_y=-2),
    Particle(x=1, y=-1, mass=1*10**11, size=50, v_x=-2),
    Particle(x=-1, y=-1, mass=1*10**11, size=50, v_y=2),
    Particle(x=-1, y=1, mass=1*10**11, size=50, v_x=2),
]