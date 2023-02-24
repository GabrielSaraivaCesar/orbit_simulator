from src import simulator
import settings
import matplotlib.pyplot as plt 
import matplotlib as mpl
import time
import numpy as np
import math

def animate_simulation(sim:simulator.Simulator, ax:plt.Axes, projection='2d'):
    anim_t = time.time()
    curr_frame_idx = 0
    """
        This function will animate a simulation based on the animation_history
    """


    def draw_simulator_frame(sim:simulator.Simulator, frame_idx:int, ax: plt.Axes):
        """
            Responsible for rendering a single frame of the animation
        """

        xl, xr = ax.get_xlim()
        yl, yr = ax.get_ylim()
        xsize = xr-xl
        ysize = yr-yl
        offset = 0.02
        zl = 0
        zr = 0
        zsize = 0
        
        if projection == '3d':
            zl, zr = ax.get_zlim()
            zsize = zr-zl

        for body_i, body in enumerate(sim.celestial_bodies):
            hist = np.array(sim.simulation_history[body_i][:frame_idx+1])


            if projection == '3d':
                zl, zr = ax.get_zlim()
                zsize = zr-zl

                ax.plot(hist[:,0],hist[:,1],hist[:,2], color=body['color'])
                ax.scatter(hist[-1][0], hist[-1][1], hist[-1][2], color=body['color'])
                if settings.SHOW_COORDS:
                    ax.text(
                        hist[-1][0] + (xsize*offset),
                        hist[-1][1] + (ysize*offset),
                        hist[-1][2] + (zsize*offset),
                        "[{:.2E}, {:.2E}, {:.2E}]".format(hist[-1][0], hist[-1][1], hist[-1][2]),
                        verticalalignment="bottom",
                        horizontalalignment="left"
                    )
            else:
                ax.plot(hist[:,0],hist[:,1], color=body['color'])
                ax.scatter(hist[-1][0], hist[-1][1], color=body['color'])
                if settings.SHOW_COORDS:
                    ax.text(
                        hist[-1][0] + (xsize*offset),
                        hist[-1][1] + (ysize*offset),
                        "[{:.2E}, {:.2E}]".format(hist[-1][0], hist[-1][1]),
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
    # Preparing canv as
    projection = "2d"
    if settings.IS_3D:
        projection = "3d"
    mpl.rcParams['toolbar'] = 'None'

    fig = plt.figure()
    fig.canvas.draw()

    ax = None
    if projection == '3d':
        ax = fig.add_subplot(projection='3d')
    else: 
        ax = fig.add_subplot()

    return (ax, fig, projection)