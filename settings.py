from src import constants
import argparse

argparser = argparse.ArgumentParser(
                    prog='orbit_simulator',
                    description='This software simulates orbital mechanics based on Newton\'s universal law of gravitation')
argparser.add_argument("preset_name")
argparser.add_argument("-3d", "--3d", action='store_true', help="Enable 3D rendering")
argparser.add_argument("-c", "--coords", action='store_true', help="Show objects coordinates")
argparser.add_argument("-s", "--speed", action='store_true', help="Show objects speeds")

args = argparser.parse_args().__dict__

FPS = 30000
RUN_TIME = constants.SECONDS_IN_ONE_HOUR*24
FRAME_TIME = 0.1

IS_3D = args['3d']
SHOW_COORDS = args['coords']
SHOW_SPEED = args['speed']


