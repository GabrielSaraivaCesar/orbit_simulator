
# Orbit Simulator
This project aims to simulate how orbital mechanics works

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

## Measurement Units
Planet mass: $kg$<br>
Distance: $m$<br>
Speed & Velocity: $m/s$<br><br>

## Assumptions and Formulas

### Gravitational Constant
This is an aproximate value of $G$ based on the paper "[Precise Ideal Value of the Universal Gravitational Constant G](https://www.scirp.org/journal/paperinformation.aspx?paperid=74770)". Writen by Abed El Karim S. Abou Layla, 2017:<br>
$G= 6.67401 \times 10^{−11} m^3 kg^{−1} s^{−2}$<br><br>

### Distance between planets
We are dealing with a 2D matrix, and planets have $x$ and $y$ coordinates. This formula gets the distance between each axis of 2 planets, interprets it as a right triangle, and then returns the hypotenuse being the distance in meters.

$\sqrt{|x_1-x_2|^{2}+|y_1-y_2|^{2}}$<br><br>

### Acceleration of Gravity
$G$ = Gravitational Constant<br>
$M$ = Target planet mass<br>
$r$ = Distance between the planets<br><br>
$g = {{G*M} \over r^{2}} $<br><br>

### Speed distribution between axis
To calculate the distribution of speed between $x$ and $y$, we need to calculate how close $x$ is from the other planet $x$ in comparison to $y$. This calculation will give us a value between $0$ and $1$, which is the proportion of the acceleration each axis should get. After that, we just need to multiply by the acceleration and $\Delta{t}$<br>
$g$ = Acceleration of gravity<br>
$\Delta{t}$ = Variation of time<br><br>
$\Delta{x} = g \times { |x_1 - x_2|\over{|x_1 - x_2|+|y_1 - y_2|} } \times \Delta{t}$ <br>
$\Delta{y} = g \times { |y_1 - y_2|\over{|x_1 - x_2|+|y_1 - y_2|} } \times \Delta{t}$ 
