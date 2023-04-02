from src import celestial_body_utils
import numpy as np
from src.presets import SimulationPreset

class Simulator:

    def __init__(self, preset:SimulationPreset):
        self.celestial_bodies:list[celestial_body_utils.CelestialBody] = preset.bodies
        self.simulation_history = [[] for _ in preset.bodies]
        self.simulation_time_tickers = []
        self.run_time = preset.run_time
        self.frame_time = preset.frame_time
        self.fps = preset.fps
        self.distance_tracers=preset.distance_tracers

    def update_frame(self):
        elapsed_time = self.simulation_time_tickers[-1] if len(self.simulation_time_tickers) > 0 else 0 
        self.simulation_time_tickers.append(self.frame_time + elapsed_time)

        for body_i, c_body in enumerate(self.celestial_bodies):
            if c_body.fixed == True: # Ignore fixed bodies
                self.simulation_history[body_i].append(c_body.pos.copy())
                continue
            
            summed_delta_v = np.array([0.0, 0.0, 0.0])
            for body_j, target_body in enumerate(self.celestial_bodies):
                if body_i == body_j: # If it's the same body, skip
                    continue

                g = celestial_body_utils.get_gravity_acceleration(c_body, target_body) # get gravity acceleration to target body
                summed_delta_v += g

            c_body.V += summed_delta_v * self.frame_time # Update velocity for each axis based on delta time
            c_body.pos += c_body.V * self.frame_time  # Update position for each axis based on velocity
            self.simulation_history[body_i].append(c_body.pos.copy())
