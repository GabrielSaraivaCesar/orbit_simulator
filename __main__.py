from matplotlib import pyplot as plt
from src.elements import Particle
import time
import src.physics as physics
import src.presets as presets
import settings

particles = presets.CHAOS

x_pathes = [[] for p in particles]
y_pathes = [[] for p in particles]


def iterate(lastFrameTime):
    current_time = time.time()
    delta_seconds = current_time - lastFrameTime
    if settings.ANIMATION_FIXED_DELTA_TIME is not None:
        delta_seconds = settings.ANIMATION_FIXED_DELTA_TIME
    
    for idx, particle in enumerate(particles):
        color_idx = idx/(len(particles)-1)

        if particle.is_fixed:
            plt.scatter(particle.x, particle.y, s=particle.size, color=plt.cm.Dark2(color_idx))
            continue
        
        # mean_x_target = 0
        # mean_y_target = 0
        # weight_sum = 0
        for other_particle_idx, other_particle in enumerate(particles):
            other_particle_color_idx = other_particle_idx/(len(particles)-1)
            if other_particle == particle:
                continue
            
            # weight_sum += other_particle.mass
            # mean_x_target += other_particle.mass*other_particle.x
            # mean_y_target += other_particle.mass*other_particle.y
                
            # mean_mass = weight_sum / (len(particles) - 1)
            # mean_x_target /= weight_sum
            # mean_y_target /= weight_sum
            
            
            # pseudo_particle = Particle(x=mean_x_target, y=mean_y_target, mass=mean_mass, size=0)
            # TODO - check if pseudo_particle with mean positions makes sense
            acceleration = physics.get_acceleration_to_target(particle, other_particle)
            x_size = abs(particle.x - other_particle.x)
            y_size = abs(particle.y - other_particle.y)
            x_acceleration_rate = (x_size/(x_size+y_size))
            y_acceleration_rate = (y_size/(x_size+y_size))
            delta_vx = acceleration * x_acceleration_rate * delta_seconds
            delta_vy = acceleration * y_acceleration_rate * delta_seconds
            
            if other_particle.y <  particle.y:
                delta_vy = -delta_vy
            if other_particle.x <  particle.x:
                delta_vx = -delta_vx
                
            if settings.DRAW_DIRECTION_LINE:
                plt.arrow(particle.x, particle.y, delta_vx*settings.DRAW_TIME_IN_FUTURE_LINE, delta_vy*settings.DRAW_TIME_IN_FUTURE_LINE, color=plt.cm.Dark2(other_particle_color_idx), width=0.002)
            
            particle.v_y += delta_vy
            particle.v_x += delta_vx
        
        
        plt.scatter(particle.x, particle.y, s=particle.size, color=plt.cm.Dark2(color_idx))
        x_pathes[idx].append(particle.x)
        y_pathes[idx].append(particle.y)
        if settings.DRAW_PATHES:
            plt.plot(x_pathes[idx], y_pathes[idx], alpha=0.3, color=plt.cm.Dark2(color_idx))
        if settings.DRAW_DIRECTION_LINE:
            plt.arrow(particle.x, particle.y, particle.v_x*settings.DRAW_TIME_IN_FUTURE_LINE, particle.v_y*settings.DRAW_TIME_IN_FUTURE_LINE, color=plt.cm.Dark2(color_idx), width=0.005)
    

        particle.move_particle(delta_seconds)
        # if settings.DRAW_UNIVERSE_CENTER_OF_MASS:
        #     plt.scatter(pseudo_particle.x, pseudo_particle.y, marker="2", color=plt.cm.Dark2(color_idx), zorder=99)
        # if settings.DRAW_LINE_TO_UNIVERSE_CENTER_OF_MASS:
        #     plt.plot([particle.x, pseudo_particle.x], [particle.y, pseudo_particle.y], color=plt.cm.Dark2(color_idx))
            
    plt.axis('equal')
    plt.draw()
    return current_time

def main():
    plt.ion()
    plt.show()
    t = time.time()
    while True:
        plt.clf()
        if len(settings.GRAPH_X_LIMITS) == 2:
            plt.xlim(settings.GRAPH_X_LIMITS)
        if len(settings.GRAPH_Y_LIMITS) == 2:
            plt.ylim(settings.GRAPH_Y_LIMITS)
        t = iterate(t)
        plt.pause(0.0001)
        

if __name__ == '__main__':
    main()