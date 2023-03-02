from src import celestial_body_utils

presets = {
    'SOLAR_SYSTEM': [
        celestial_body_utils.CelestialBody(mass=1.989e30,  fixed=True, name='Sun', color='orange'),
        celestial_body_utils.CelestialBody(mass=0.33e24, x=46.00e9, vy=58.98e3, name='Mercury'),
        celestial_body_utils.CelestialBody(mass=4.8673e24, x=1.0748e11, vy=35.26e3, name='Venus'),
        celestial_body_utils.CelestialBody(mass=5.9722e24, x=1.470e11, vy=30.29e3, name='Earth', color='green'),
        celestial_body_utils.CelestialBody(mass=0.64169e24, x=2.06650e11, vy=26.50e3, name='Mars', color='red'),
    ],

    'SYNCHRONOUS_ORBITS': [
        celestial_body_utils.CelestialBody(y=147e9, vx=30300/2),
        celestial_body_utils.CelestialBody(y=-147e9, vx=-30300/2),
        celestial_body_utils.CelestialBody(x=147e9, vy=-30300/2),
        celestial_body_utils.CelestialBody(x=-147e9, vy=30300/2),
        celestial_body_utils.CelestialBody(mass=1.989e30, fixed=True),
    ],
    
    'HIGH_INFLUENCES': [
        celestial_body_utils.CelestialBody(x=0, y=147e9/2, mass=1.989e28, vx=30300/2),
        
        celestial_body_utils.CelestialBody(x=0, y=147e9/4, mass=1.989e28/2, vx=30300),
        celestial_body_utils.CelestialBody(mass=1.989e30/2, fixed=True),
    ],
}
