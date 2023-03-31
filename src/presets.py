from src import celestial_body_utils
import settings
from src import constants

class SimulationPreset():
    def __init__(self, bodies=[], run_time=settings.RUN_TIME, frame_time=settings.FRAME_TIME, fps=settings.FPS, distance_tracers=[]):
        self.bodies=bodies
        self.run_time=run_time
        self.frame_time=frame_time
        self.fps=fps
        self.distance_tracers=distance_tracers

presets = {
    'SIMPLE_ORBIT': SimulationPreset(
        bodies=[
            celestial_body_utils.CelestialBody(mass=1.989e30,  fixed=True, name='Sun', color='orange'),
            celestial_body_utils.CelestialBody(mass=5.9722e24, x=1.470e11, vy=30.29e3, name='Earth', color='green'),
        ]
    ),

    'SOLAR_SYSTEM': SimulationPreset(
        run_time=constants.SECONDS_IN_ONE_YEAR*10,
        frame_time=constants.SECONDS_IN_ONE_DAY,
        fps=30,
        bodies=[
            celestial_body_utils.CelestialBody(mass=1.989e30,  fixed=True, name='Sun', color='orange'),
            celestial_body_utils.CelestialBody(mass=0.33e24, x=46.00e9, vy=58.98e3, name='Mercury'),
            celestial_body_utils.CelestialBody(mass=4.8673e24, x=1.0748e11, vy=35.26e3, name='Venus'),
            celestial_body_utils.CelestialBody(mass=5.9722e24, x=1.470e11, vy=30.29e3, name='Earth', color='green'),
            celestial_body_utils.CelestialBody(mass=0.64169e24, x=2.06650e11, vy=26.50e3, name='Mars', color='red'),
        ],
        distance_tracers=[[0, 3]]
    ),

    'SYNCHRONOUS_ORBITS': SimulationPreset(
        bodies=[
            celestial_body_utils.CelestialBody(y=147e9, vx=30300/2),
            celestial_body_utils.CelestialBody(y=-147e9, vx=-30300/2),
            celestial_body_utils.CelestialBody(x=147e9, vy=-30300/2),
            celestial_body_utils.CelestialBody(x=-147e9, vy=30300/2),
            celestial_body_utils.CelestialBody(mass=1.989e30, fixed=True),
        ]
    ),
    

    'SYNCHRONOUS_ORBITS_2': SimulationPreset(
        run_time=constants.SECONDS_IN_ONE_DAY,
        frame_time=1,
        fps=5000,
        bodies=[
            celestial_body_utils.CelestialBody(y=42_164_000, vx=3074.6),
            celestial_body_utils.CelestialBody(mass=5.9722e24, x=0, vy=0, fixed=True, name='Earth', color='green'),
        ],
        distance_tracers=[[0,1]]
    ),

    'HIGH_INFLUENCES': SimulationPreset(
        bodies=[
            celestial_body_utils.CelestialBody(x=0, y=147e9/2, mass=1.989e28, vx=30300/2),
            
            celestial_body_utils.CelestialBody(x=0, y=147e9/4, mass=1.989e28/2, vx=30300),
            celestial_body_utils.CelestialBody(mass=1.989e30/2, fixed=True),
        ]
    ),
}
