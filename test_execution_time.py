from src import simulator
from src.presets import presets
import settings

time_list = []

for i in range(10):
    sim = simulator.Simulator(presets[settings.args['preset_name'].upper()])
    sim_time = simulator.simulate(sim)
    time_list.append(sim_time)


avg = sum(time_list) / len(time_list)
print("Average execution time: {:.2f}s".format(avg))