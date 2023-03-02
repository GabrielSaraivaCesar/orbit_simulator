from src import simulator
import settings
import matplotlib.pyplot as plt 
import matplotlib as mpl
import time
import numpy as np
import math

def animate_simulation(sim:simulator.Simulator, ax:plt.Axes):
    """
        This function will animate a simulation based on the animation_history
    """
    # Initialize animation variables
    anim_t = time.time()
    curr_frame_idx = 0

    def draw_simulator_frame(sim:simulator.Simulator, frame_idx:int, ax: plt.Axes):
        """
            Responsible for rendering a single frame of the animation
        """

        x_left, x_right = ax.get_xlim()
        x_size = x_right-x_left

        y_left, y_right = ax.get_ylim()
        y_size = y_right-y_left

        text_pos_offset = 0.02

        z_left, z_right = ax.get_zlim() if settings.IS_3D else (0, 0)
        z_size = z_right-z_left

        for body_i, body in enumerate(sim.celestial_bodies):
            hist = np.array(sim.simulation_history[body_i][:frame_idx+1])
            
            plot_coords = np.array(hist[:,0],hist[:,1],hist[:,2]) if settings.IS_3D else np.array([hist[:,0],hist[:,1]])
            text_coords = (np.array(hist[:,0] + (x_size*text_pos_offset),
                                   hist[:,1] + (y_size*text_pos_offset),
                                   hist[:,2] + (z_size*text_pos_offset)) 
                            if settings.IS_3D else 
                            np.array([hist[:,0] + (x_size*text_pos_offset),  hist[:,1] + (y_size*text_pos_offset)]))[:,-1]
            
            ax.plot(*plot_coords, color=body.color)
            if body.radius is None:
                ax.scatter(*(plot_coords[:,-1]), color=body.color)
            else:
                circle = plt.Circle((plot_coords[:,-1]), body.radius, color=body.color)
                ax.add_patch(circle)

            if settings.SHOW_COORDS and body.fixed is False:
                ax.text(
                    *text_coords,
                    "[{:.2E}, {:.2E}, {:.2E}]".format(plot_coords[0][-1], plot_coords[1][-1], plot_coords[2][-1]) if settings.IS_3D else "[{:.2E}, {:.2E}]".format(plot_coords[0][-1], plot_coords[1][-1]),
                    verticalalignment="bottom",
                    horizontalalignment="left"
                )
                

    def uptate_execution_time_text(frame_index):
        """
            This function updates plot title to show how many times the time is accelerated and the current simulation time delta
        """
        execution_time = sim.simulation_time_tickers[frame_index]
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
        ax.set_title("{0}x ({1})".format(settings.FRAME_TIME, '{days_text}{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds), days_text=days_text), ))

    
    while True:
        anim_dt = time.time() - anim_t

        curr_frame_idx = math.ceil(anim_dt/(1/settings.FPS))

        if curr_frame_idx > len(sim.simulation_history[0])-1:
            anim_t = time.time()
            curr_frame_idx = 0

        ax.clear()
        plt.axis('equal')

        uptate_execution_time_text(curr_frame_idx)
        draw_simulator_frame(sim, curr_frame_idx, ax)

        plt.pause(0.0000000001)


def set_up_mpl():
    # Preparing canvas
    mpl.rcParams['toolbar'] = 'None'

    fig = plt.figure()
    fig.canvas.draw()

    ax = fig.add_subplot(projection='3d') if settings.IS_3D else fig.add_subplot()

    return (ax, fig)