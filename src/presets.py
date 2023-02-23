from src import celestial_body_utils

presets = {
    'EARTH': [
        celestial_body_utils.create_celestial_body(mass=1.989e30,  fixed=True), # sun
        celestial_body_utils.create_celestial_body(mass=5.972e24, x=147e9, vy=30300), # earth
    ],

    'SYNCHRONOUS_ORBITS': [
        celestial_body_utils.create_celestial_body(y=147e9, vx=30300/3),
        celestial_body_utils.create_celestial_body(y=-147e9, vx=-30300/3),
        celestial_body_utils.create_celestial_body(x=147e9, vy=-30300/3),
        celestial_body_utils.create_celestial_body(x=-147e9, vy=30300/3),
        celestial_body_utils.create_celestial_body(mass=1.989e30, fixed=True),
    ],
    
    'HIGH_INFLUENCES': [
        celestial_body_utils.create_celestial_body(x=0, y=147e9/2, mass=1.989e28, vx=30300/2),
        
        celestial_body_utils.create_celestial_body(x=0, y=147e9/4, mass=1.989e28/2, vx=30300),
        celestial_body_utils.create_celestial_body(mass=1.989e30/2, fixed=True),
    ],
}
