from matplotlib import pyplot as plt
import time
import src.physics as physics
import src.presets as presets
import settings
import math
import argparse

arg_parser = argparse.ArgumentParser(
                    prog = 'orbit_simulator',
                    description = 'This project aims to simulate how orbital mechanics works'
                    )
arg_parser.add_argument('preset', help="Simulation preset name", type=str, choices=presets.presets_object.keys())   
arg_parser.add_argument('-mp', '--path-size', default=10000, type=int, help="Maximum amount of path coordinates")
arg_parser.add_argument('-p', '--no-pathes', action='store_true', help="Disable path drawing")
arg_parser.add_argument('-d', '--direction', action='store_true', help="Allow direction drawing")
arg_parser.add_argument('-tw', '--time-warp', default=1, type=float, help="Sets time warp")
arg_parser.add_argument('-ei', '--extra-iterations', default=10, type=float, help="Extra interaction per loop. Increases precision. Decreases performance")
arg_parser.add_argument('-fps', '--fps', default=30, type=float, help="Sets the frame rate. Decreases performance")
arg_parser.add_argument('-3d', '--3d', action='store_true', help="Force 3d rendering", dest="force_3d")


preset = "SIMPLE_ORBIT"
planets = []

x_pathes = []
y_pathes = []
z_pathes = []

max_x = 0
min_x = 0
max_y = 0
min_y = 0
max_z = 0
min_z = 0

projection = "2d"
fig = None
ax = None
renderer = None
angle_3d = 0

def is_3d_projection():
    return projection == '3d'

def iterate(delta_seconds, draw):
    
    for idx, planet in enumerate(planets):

        if planet.is_fixed:
            continue
        
        for other_planet_idx, other_planet in enumerate(planets):
            other_planet_color_idx = other_planet_idx/(len(planets)-1)
            if other_planet == planet:
                continue
            
            # Get gravity acceleration related to the planet
            acceleration = physics.get_acceleration_to_target(planet, other_planet)
            x_size = abs(planet.x - other_planet.x)
            y_size = abs(planet.y - other_planet.y)
            z_size = 0
            if projection == '3d':
                z_size = abs(planet.z - other_planet.z)
            x_acceleration_rate = (x_size/(x_size+y_size+z_size))
            y_acceleration_rate = (y_size/(x_size+y_size+z_size))
            

            delta_vx = acceleration * x_acceleration_rate * delta_seconds
            delta_vy = acceleration * y_acceleration_rate * delta_seconds
            if other_planet.y <  planet.y:
                delta_vy = -delta_vy
            if other_planet.x <  planet.x:
                delta_vx = -delta_vx

            
            if projection == '3d':
                z_acceleration_rate = (z_size/(x_size+y_size+z_size))
                delta_vz = acceleration * z_acceleration_rate * delta_seconds
                if other_planet.z <  planet.z:
                    delta_vz = -delta_vz
                planet.v_z += delta_vz
                
            # if settings.DRAW_DIRECTION_LINE:
            #     if draw:
            #         plt.arrow(planet.x, planet.y, delta_vx*settings.DRAW_TIME_IN_FUTURE_LINE*20, delta_vy*settings.DRAW_TIME_IN_FUTURE_LINE*20, color=plt.cm.Dark2(other_planet_color_idx), width=0.002)
            
            planet.v_y += delta_vy
            planet.v_x += delta_vx
        
        if settings.DRAW_PATHES and draw:
            x_pathes[idx].append(planet.x)
            y_pathes[idx].append(planet.y)
            z_pathes[idx].append(planet.z)
            
                
        planet.move_planet(delta_seconds)

        


def draw_frame():
    global min_x, max_x, min_y, max_y, max_z, min_z
    global x_pathes, y_pathes, z_pathes

    for idx, planet in enumerate(planets):
        color_idx = idx/(len(planets)-1)
        color = plt.cm.Dark2(color_idx)
        if planet.color:
            color = planet.color

        if projection == '3d':
            ax.view_init((math.sin(angle_3d/10)+1)*(25-10)+10, angle_3d)
            ax.scatter(planet.x, planet.y, planet.z, s=planet.size, color=color)
        else:
            ax.scatter(planet.x, planet.y, s=planet.size, color=color)

        if planet.is_fixed:
            continue

        
        if settings.DRAW_PATHES:
            x_pathes[idx] = x_pathes[idx][-settings.MAX_PATH_SIZE:]
            y_pathes[idx] = y_pathes[idx][-settings.MAX_PATH_SIZE:]
            z_pathes[idx] = z_pathes[idx][-settings.MAX_PATH_SIZE:]
            if projection == '3d':
                ax.plot(x_pathes[idx], y_pathes[idx], z_pathes[idx], alpha=0.3, color=color)
            else: 
                ax.plot(x_pathes[idx], y_pathes[idx], alpha=0.3, color=color)
        if settings.DRAW_DIRECTION_LINE:
            if projection == '3d':
                ax.arrow(planet.x, planet.y, planet.z, planet.v_x*settings.DRAW_TIME_IN_FUTURE_LINE, planet.v_y*settings.DRAW_TIME_IN_FUTURE_LINE, planet.v_z*settings.DRAW_TIME_IN_FUTURE_LINE, color=color, width=0.005)
            else:
                ax.arrow(planet.x, planet.y, planet.v_x*settings.DRAW_TIME_IN_FUTURE_LINE, planet.v_y*settings.DRAW_TIME_IN_FUTURE_LINE, color=color, width=0.005)

        if planet.x > max_x:
            max_x = planet.x
        elif planet.x < min_x:
            min_x = planet.x
            
        if planet.y > max_y:
            max_y = planet.y
        elif planet.y < min_y:
            min_y = planet.y
            
        if projection == '3d':
            if planet.z > max_z:
                max_z = planet.z
            elif planet.z < min_z:
                min_z = planet.z
        
    if is_3d_projection():
        ax.scatter(max_x, max_y, max_z, color="#00000000")
        ax.scatter(min_x, min_y, min_z, color="#00000000")
    else:
        ax.scatter(max_x, max_y, color="#00000000")
        ax.scatter(min_x, min_y, color="#00000000")

    plt.axis('equal')
    ax.draw(renderer)

def main():
    global angle_3d
    iteration_t = time.time()
    drawing_t = time.time()
    while True:
        iteration_delta_t = time.time() - iteration_t
        iteration_t = time.time()
        drawing_delta_t = time.time() - drawing_t
        time_to_draw = False

        ax.clear()

        if drawing_t >= 1/settings.FPS:
            time_to_draw = True
            drawing_t = time.time()

        iterations_number = math.ceil(math.ceil(settings.TIME_WARP) * settings.ITERATIONS_PER_TICK)
        for i in range(iterations_number):
            progress = (i+1)/iterations_number
            iterate((iteration_delta_t  * settings.TIME_WARP)/iterations_number, time_to_draw and progress == 1)

        if time_to_draw:
            angle_3d += settings.ROTATION_3D_RATE * drawing_delta_t 
            draw_frame()
        ax.set_title("{0} -> {1}x".format(preset, settings.TIME_WARP))
        plt.pause(0.000000001)
        


if __name__ == '__main__':
    args = arg_parser.parse_args()
    settings.DRAW_DIRECTION_LINE = args.direction
    settings.DRAW_PATHES = not args.no_pathes 
    settings.FPS = args.fps
    settings.TIME_WARP = args.time_warp
    settings.ITERATIONS_PER_TICK = args.extra_iterations
    preset = args.preset
    planets = presets.get_preset_by_name(preset)

    if presets.is_preset_3d(planets) or args.force_3d:
        projection = "3d"
        presets.normalize_3d_preset(planets)
        
    fig = plt.figure()
    fig.canvas.draw()
    if is_3d_projection():
        ax = fig.add_subplot(projection=projection)
    else:
        ax = fig.add_subplot()
        
    renderer = fig.canvas.renderer

    x_pathes = [[] for p in planets]
    y_pathes = [[] for p in planets]
    z_pathes = [[] for p in planets]
    main()