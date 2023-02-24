from src import celestial_body_utils

presets = {
    'SOLAR_SYSTEM': [
        celestial_body_utils.create_celestial_body(mass=1.989e30,  fixed=True, name='Sun', color='orange'),
        celestial_body_utils.create_celestial_body(mass=0.330e24, x=46e9, vy=58_980, name='Mercury'),
        celestial_body_utils.create_celestial_body(mass=4.8673e24, x=107_480e6, vy=35_260, name='Venus'),
        celestial_body_utils.create_celestial_body(mass=5.9722e24, x=147e9, vy=30_300, name='Earth', color='green'),
        celestial_body_utils.create_celestial_body(mass=0.64169e24, x=206_650e6, vy=26_500, name='Mars', color='red'),
        # celestial_body_utils.create_celestial_body(mass=1898.13e24, x=740_595e6, vy=13_720, name='Jupiter'),
    ],

    'SYNCHRONOUS_ORBITS': [
        celestial_body_utils.create_celestial_body(y=147e9, vx=30300/2),
        celestial_body_utils.create_celestial_body(y=-147e9, vx=-30300/2),
        celestial_body_utils.create_celestial_body(x=147e9, vy=-30300/2),
        celestial_body_utils.create_celestial_body(x=-147e9, vy=30300/2),
        celestial_body_utils.create_celestial_body(mass=1.989e30, fixed=True),
    ],
    
    'HIGH_INFLUENCES': [
        celestial_body_utils.create_celestial_body(x=0, y=147e9/2, mass=1.989e28, vx=30300/2),
        
        celestial_body_utils.create_celestial_body(x=0, y=147e9/4, mass=1.989e28/2, vx=30300),
        celestial_body_utils.create_celestial_body(mass=1.989e30/2, fixed=True),
    ],
}
