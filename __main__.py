import sys
from src import simulator, rendering
from src.presets import presets
import settings

ax, fig = rendering.set_up_matplotlib()


def on_close(_):
    sys.exit()


def are_args_valid():
    if not settings.args['preset_name'].upper() in presets:
        preset_list_str = ""
        for preset_key in presets.keys():
            preset_list_str += "{0}\n".format(preset_key)

        print("Preset \"{0}\" doesn't exist, available presets: \n{1}".format(settings.args['preset_name'], preset_list_str ))
        return False
    return True


if __name__ == '__main__':
    if not are_args_valid():
        exit()

    sim = simulator.Simulator(presets[settings.args['preset_name'].upper()])
    renderer = rendering.SimulationRenderer(sim, ax)

    fig.canvas.mpl_connect('close_event', on_close)    
    simulator.simulate(sim)
    renderer.animate_simulation()
    