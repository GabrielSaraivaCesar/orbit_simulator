
# Orbit Simulator
This project aims to simulate how orbital mechanics work

## Examples
<table cellspacing="0" cellpadding="0">
  <tr>
    <td><img src="./readme_files/simple_orbit.gif" alt="Simple orbit" /></td>
    <td><img src="./readme_files/simple_orbit_2.gif" alt="Simple orbit with 2 planets"/></td>
    <td><img src="./readme_files/too_close.gif" alt="Orbit with 2 massive objects too close"/></td>
    <td><img src="./readme_files/sync.gif" alt="Synchronous orbit of 4 planets"/></td>
  </tr>
  <tr>
    <td>Simple orbit</td>
    <td>Simple orbit with 2 planets</td>
    <td>Orbit with 2 massive objects too close</td>
    <td>Synchronous orbit of 4 planets</td>
  </tr>
</table>

## Features
You can configure a set of things in the settings.py file like:
|Config name|Description|Value type|
|-----------|-----------|----------|
|DRAW_PATHES|Shows the previous path of each planet|Boolean|
|DRAW_DIRECTION_LINE|Shows lines of directional moment of inertia and gravitational influences|Boolean|
|TIME_WARP|Changes the speed of the simulation in relation with real life time. This will not affect the render rate|Float|
|ITERATIONS_PER_TICK|Sets how many iterations you want for each loop. Useful to increase precision in high TIME_WARPs|Float|
|FPS|Sets the maximum frame rate of the animation. Lower FPSs will increase performance|Float|
### Execution
```
usage: orbit_simulator [-h] [-mp PATH_SIZE] [-p] [-d] [-tw TIME_WARP]
                       [-ei EXTRA_ITERATIONS] [-fps FPS]
                       preset

This project aims to simulate how orbital mechanics works

positional arguments:
  preset                Simulation preset name

options:
  -h, --help            show this help message and exit
  -mp PATH_SIZE, --path-size PATH_SIZE
                        Maximum amount of path coordinates
  -p, --no-pathes       Disable path drawing
  -d, --direction       Allow direction drawing
  -tw TIME_WARP, --time-warp TIME_WARP
                        Sets time warp
  -ei EXTRA_ITERATIONS, --extra-iterations EXTRA_ITERATIONS
                        Extra interaction per loop. Increases precision.
                        Decreases performance
  -fps FPS, --fps FPS   Sets the frame rate. Decreases performance
```

## Measurement Units
Planet mass: $kg$<br>
Distance: $m$<br>
Speed & Velocity: $m/s$<br><br>

## Assumptions and Formulas

### Gravitational Constant
This is an aproximate value of $G$ based on the paper "[Precise Ideal Value of the Universal Gravitational Constant G](https://www.scirp.org/journal/paperinformation.aspx?paperid=74770)". Writen by Abed El Karim S. Abou Layla, 2017:<br>
$G= 6.67401 \times 10^{−11} m^3 kg^{−1} s^{−2}$<br><br>

### Distance between planets
We are dealing with a 2D matrix, and planets have $x$ and $y$ coordinates. This formula gets the distance between each axis of 2 planets by interpreting it as a right triangle, and then returning the hypotenuse being the distance in meters.

$\sqrt{|x_1-x_2|^{2}+|y_1-y_2|^{2}}$<br><br>

### Acceleration of Gravity
$G$ = Gravitational Constant<br>
$M$ = Target planet mass<br>
$r$ = Distance between the planets<br><br>
$g = {{G*M} \over r^{2}} $<br><br>

### Speed distribution between axis
To calculate the distribution of speed between $x$ and $y$, we need to calculate how close $x$ is from the other planet $x$ in comparison to $y$. This calculation will give us a value between $0$ and $1$, which is the proportion of the acceleration each axis should get. After that, we just need to multiply it by the acceleration and $\Delta{t}$<br>
$g$ = Acceleration of gravity<br>
$\Delta{t}$ = Variation of time<br><br>
$\Delta{x} = g \times { |x_1 - x_2|\over{|x_1 - x_2|+|y_1 - y_2|} } \times \Delta{t}$ <br>
$\Delta{y} = g \times { |y_1 - y_2|\over{|x_1 - x_2|+|y_1 - y_2|} } \times \Delta{t}$ 

