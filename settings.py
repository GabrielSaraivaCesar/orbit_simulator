
DRAW_PATHES=True
MAX_PATH_SIZE=10000 # Can be none if you want to keep drawing
DRAW_DIRECTION_LINE=False
DRAW_TIME_IN_FUTURE_LINE=1

# This will make simulation behind the scenes faster. But keeping the draw rate. If it's too high, pathes might look weird
TIME_WARP=2

# This defines the amount of divisions you will make per iterations. If 10 => Divide delta time by 10 and iterate 10 times
# Important to make the calculations right maily with high TIME_WARP values and/or planets getting to close from others
ITERATIONS_PER_TICK=10

# Defines a maximum frame rate per second. Simulation will not be affected by this value, only rendering
FPS = 15