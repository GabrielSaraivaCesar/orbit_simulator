import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import settings
import time
import sys
from src import celestial_body_utils, simulator
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Preparing canvas
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
renderer = fig.canvas.renderer

sim = simulator.Simulator([
    celestial_body_utils.create_celestial_body(mass=1.989e30,  fixed=True), # sun
    celestial_body_utils.create_celestial_body(mass=5.972e24, x=147e9, vy=30300), # earth
])

def simulate():
    """
        This function will generate the animation and store it into Simulator.simulation_history
    """
    t = np.arange(0.0, settings.RUN_TIME, settings.FRAME_TIME) # This will generate time tickers
    for _ in t:
        sim.update_frame(settings.FRAME_TIME)

 
def animate_simulation(sim:simulator.Simulator, ax:plt.Axes):
    anim_t = time.time()
    curr_frame_idx = 0
    """
        This function will animate a simulation based on the animation_history
    """


    def draw_simulator_frame(sim:simulator.Simulator, frame_idx:int, ax: plt.Axes):
        """
            Responsible for rendering a single frame of the animation
        """

        for body_i, body in enumerate(sim.celestial_bodies):
            hist = np.array(sim.simulation_history[body_i][:frame_idx+1])

            if projection == '3d':
                ax.plot(hist[:,0],hist[:,1],hist[:,2])
                ax.scatter(hist[-1][0], hist[-1][1], hist[-1][2])
            else:
                ax.plot(hist[:,0],hist[:,1])
                ax.scatter(hist[-1][0], hist[-1][1])
                

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
        if anim_dt >= 1/settings.FPS: # Time to draw

            ax.clear()
            plt.axis('equal')

            uptate_execution_time_text(curr_frame_idx)
            draw_simulator_frame(sim, curr_frame_idx, ax)

            plt.pause(0.0000000001)

            anim_t = time.time()
            curr_frame_idx += 1
            if curr_frame_idx > len(sim.simulation_history[0])-1:
                curr_frame_idx = 0
            

def on_close(_):
    sys.exit()


if __name__ == '__main__':
    fig.canvas.mpl_connect('close_event', on_close)
    
    simulate()
    animate_simulation(sim, ax)
    