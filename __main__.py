import numpy as np
import settings
import time
import sys
from src import simulator, rendering
from src.presets import presets
import math


ax, fig = rendering.set_up_mpl()
sim = simulator.Simulator(presets['HIGH_INFLUENCES'])

coordinate_shower_position = None

def simulate():
    """
        This function will generate the animation and store it into Simulator.simulation_history
    """
    sim_time = time.time()
    t = np.arange(0.0, settings.RUN_TIME, settings.FRAME_TIME) # This will generate time tickers
    print("Generating simulation [0/{0}] (0%)".format(len(t)), end='\r')
    for idx, _ in enumerate(t):
        sim.update_frame(settings.FRAME_TIME)
        if idx % math.ceil(len(t)/100) == 0:
            print("Generating simulation [{0}/{1}] ({2}%)".format(idx, len(t), int(idx/len(t)*100)), end='\r')

    print("Generating simulation [{0}/{0}] (100%)".format(len(t)))
    print("Simulation generated in {0:.2f}s".format(time.time() - sim_time))

def on_close(_):
    sys.exit()

if __name__ == '__main__':
    fig.canvas.mpl_connect('close_event', on_close)    
    simulate()
    rendering.animate_simulation(sim, ax)
    