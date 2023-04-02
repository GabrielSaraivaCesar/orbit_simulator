from src import simulator, celestial_body_utils
import settings
import matplotlib.pyplot as plt 
import matplotlib as mpl
import time
import numpy as np
import math

class SimulationRenderer():
    def __init__(self, sim:simulator.Simulator, ax: plt.Axes):
        self.sim = sim
        self.ax = ax


    def _draw_distance_tracers(self, frame_idx:int):
        for tracer in self.sim.distance_tracers:
            t_0_pos = self.sim.simulation_history[tracer[0]][frame_idx+1]
            t_1_pos = self.sim.simulation_history[tracer[1]][frame_idx+1]
            dist = math.sqrt(
                    np.sum(
                        np.power(
                            t_0_pos - t_1_pos, 
                            2
                        )
                    )
                )

            if settings.IS_3D:
                self.ax.plot([t_0_pos[0], t_1_pos[0]], [t_0_pos[1], t_1_pos[1]], [t_0_pos[2], t_1_pos[2]], '--', alpha=0.2, color="black")
                self.ax.text(
                    (t_0_pos[0] + t_1_pos[0]) / 2,
                    (t_0_pos[1] + t_1_pos[1]) / 2,
                    (t_0_pos[2] + t_1_pos[2]) / 2,
                    "{:.2E}m".format(dist)
                )
            else:
                self.ax.plot([t_0_pos[0], t_1_pos[0]], [t_0_pos[1], t_1_pos[1]], '--', alpha=0.2, color="black")
                self.ax.text(
                    (t_0_pos[0] + t_1_pos[0]) / 2,
                    (t_0_pos[1] + t_1_pos[1]) / 2,
                    "{:.2E}m".format(dist)
                )


    def _draw_simulator_frame(self, frame_idx:int):
        """
            Responsible for rendering a single frame of the animation
        """

        x_left, x_right = self.ax.get_xlim()
        x_size = x_right-x_left

        y_left, y_right = self.ax.get_ylim()
        y_size = y_right-y_left

        text_pos_offset = 0.02

        z_left, z_right = self.ax.get_zlim() if settings.IS_3D else (0, 0)
        z_size = z_right-z_left

        self._draw_distance_tracers(frame_idx)


        for body_i, body in enumerate(self.sim.celestial_bodies):
            hist = np.array(self.sim.simulation_history[body_i][:frame_idx+1])
            
            plot_coords = np.array([hist[:,0],hist[:,1],hist[:,2]]) if settings.IS_3D else np.array([hist[:,0],hist[:,1]])
            text_coords = (np.array([hist[:,0] + (x_size*text_pos_offset),
                                    hist[:,1] + (y_size*text_pos_offset),
                                    hist[:,2] + (z_size*text_pos_offset)]) 
                            if settings.IS_3D else 
                            np.array([hist[:,0] + (x_size*text_pos_offset),  hist[:,1] + (y_size*text_pos_offset)]))[:,-1]
            
            self.ax.plot(*plot_coords, color=body.color)
            
            if body.radius is None:
                self.ax.scatter(*(plot_coords[:,-1]), color=body.color)
            else:
                circle = plt.Circle((plot_coords[:,-1]), body.radius, color=body.color)
                self.ax.add_patch(circle)

            if settings.SHOW_COORDS and not settings.SHOW_SPEED and body.fixed is False:
                self.ax.text(
                    *text_coords,
                    "[{:.2E}, {:.2E}, {:.2E}]".format(plot_coords[0][-1], plot_coords[1][-1], plot_coords[2][-1]) if settings.IS_3D else "[{:.2E}, {:.2E}]".format(plot_coords[0][-1], plot_coords[1][-1]),
                    verticalalignment="bottom",
                    horizontalalignment="left"
                )
            elif not settings.SHOW_COORDS and settings.SHOW_SPEED and body.fixed is False:
                self.ax.text(
                    *text_coords,
                    "{:.2f}m/s".format(celestial_body_utils.get_celestial_body_speed(body)),
                    verticalalignment="bottom",
                    horizontalalignment="left"
                )


    def _uptate_execution_time_text(self, frame_idx:int):
        """
            This function updates plot title to show how many times the time is accelerated and the current simulation time delta
        """
        execution_time = self.sim.simulation_time_tickers[frame_idx]
        days, remainder = divmod(execution_time, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        days_text = ''
        if days > 0:
            days_text = '{:02} '.format(int(days))
            if days > 1:
                days_text += 'days '
            else:
                days_text += 'day '

        # This will show the elapsed time of the simulation (considering time warp)
        self.ax.set_title("{0}x ({1})".format(self.sim.frame_time * self.sim.fps, '{days_text}{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds), days_text=days_text), ))

                
    def animate_simulation(self):
        """
            This function will animate a simulation based on the animation_history
        """
        # Initialize animation variables
        anim_t = time.time()
        curr_frame_idx = 0

        
        while True:
            anim_dt = time.time() - anim_t

            curr_frame_idx = math.ceil(anim_dt/(1/self.sim.fps))

            if curr_frame_idx > len(self.sim.simulation_history[0])-1:
                anim_t = time.time()
                curr_frame_idx = 0

            self.ax.clear()
            plt.axis('equal')

            self._uptate_execution_time_text(curr_frame_idx)
            self._draw_simulator_frame(curr_frame_idx)

            plt.pause(0.0000000001)


def set_up_matplotlib():
    # Preparing canvas
    mpl.rcParams['toolbar'] = 'None'

    fig = plt.figure()
    fig.canvas.draw()

    ax = fig.add_subplot(projection='3d') if settings.IS_3D else fig.add_subplot()

    return (ax, fig)