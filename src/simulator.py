from src import celestial_body_utils
import numpy as np

class Simulator:
    simulation_history = []
    simulation_time_tickers = []
    celestial_bodies = []

    def __init__(self, celestial_bodies):
        self.celestial_bodies = celestial_bodies
        self.simulation_history = [[] for _ in celestial_bodies]

    def update_frame(self, delta_time):
        elapsed_time = 0
        if len(self.simulation_time_tickers) > 0:
            elapsed_time = self.simulation_time_tickers[-1]
        self.simulation_time_tickers.append(delta_time + elapsed_time)

        for body_i, from_body in enumerate(self.celestial_bodies):
            if from_body['fixed'] == True: # Ignore fixed bodies
                self.simulation_history[body_i].append(from_body['pos'].copy())
                continue
            
            summed_delta_v = np.array([0, 0, 0])
            for body_j, target_body in enumerate(self.celestial_bodies):

                if body_i == body_j: # If it's the same body, skip
                    continue

                g = celestial_body_utils.get_gravity_acceleration(from_body, target_body) # get gravity acceleration to target body
                
                summed_delta_v = summed_delta_v + g

            from_body['V'] += summed_delta_v * delta_time # Update velocity for each axis based on delta time
            from_body['pos'] += from_body['V'] * delta_time  # Update position for each axis based on delta time

            self.simulation_history[body_i].append(from_body['pos'].copy())