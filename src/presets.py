from src.elements import Particle

SIMPLE_ORBIT = [
    Particle(x=0, y=1, mass=1, size=50, v_x=0.3),
    Particle(x=0, y=0, mass=1*10**10, size=50**2, is_fixed=True),
]
SIMPLE_ORBIT_2 = [
    Particle(x=0.5, y=1.5, mass=0, size=20, v_x=0.45, v_y=0),
    Particle(x=0, y=1, mass=1*10**9, size=50, v_x=0.3),
]

INERTIA_DEMO = [
    Particle(x=0, y=0.5, mass=1*10**3, size=50, v_x=0.2),
    Particle(x=0, y=0, mass=1*10**9, size=50, is_fixed=True),
]

INERTIA_DEMO_2 = [
    Particle(x=0, y=0.5, mass=1*10**3, size=50),
    Particle(x=0, y=0, mass=1*10**9, size=50, is_fixed=True),
]


INERTIA_DEMO_3 = [
    Particle(x=0, y=0.5, mass=0, size=50),
    Particle(x=-0.5, y=0, mass=1*10**9, size=50, is_fixed=True),
    Particle(x=0.5, y=0, mass=1.5*10**9, size=50, is_fixed=True),
]


INERTIA_DEMO_4 = [
    Particle(x=1, y=0.5, mass=0, size=50),
    Particle(x=-0.5, y=0, mass=1*10**9, size=50, is_fixed=True),
    Particle(x=0.5, y=0, mass=1*10**9, size=50, is_fixed=True),
]


CHAOS = [
    Particle(x=0.5, y=0.5, mass=1*10**9, size=50, v_x=0.1),
    Particle(x=0, y=-0.5, mass=1*10**9, size=50, v_x=-0.1),
    Particle(x=0.5, y=0, mass=1*10**9, size=50, v_y=-0.1),
    Particle(x=-0.5, y=0, mass=1*10**9, size=50, v_y=-0.1),
    Particle(x=0, y=0, mass=1*10**9, size=100, is_fixed=True),
]

CHAOS_2 = [
    Particle(x=0, y=0.5, mass=1*10**9, size=50, v_x=0.1),
    Particle(x=0.5, y=0, mass=1*10**9, size=50, v_y=-0.1),
    Particle(x=0, y=-0.5, mass=1*10**9, size=50, v_x=-0.1),
    Particle(x=-0.5, y=0, mass=1*10**9, size=50, v_y=0.1),
    Particle(x=0, y=0, mass=1*10**9, size=50),
]

CHAOS_3 = [
    Particle(x=0, y=0.5, mass=0, size=50, v_x=0.1),
    Particle(x=0.5, y=0, mass=0, size=50, v_y=-0.1),
    Particle(x=0, y=-0.5, mass=0, size=50, v_x=-0.1),
    Particle(x=-0.5, y=0, mass=0, size=50, v_y=0.1),
    Particle(x=0, y=0, mass=1*10**10, size=100, is_fixed=True),
]


SINE = [
    Particle(x=0, y=0, mass=1*10**9, size=50, v_x=0.1),
    Particle(x=0, y=0.5, mass=1, size=50, v_x=0.1),
]
SINE_2 = [
    Particle(x=0, y=0, mass=1*10**9, size=50, v_x=0.1),
    Particle(x=0, y=0.5, mass=1*10**9, size=50, v_x=0.1),
]
