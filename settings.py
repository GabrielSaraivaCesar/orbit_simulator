
DRAW_PATHES=True
MAX_PATH_SIZE=10000 # Can be none if you want to keep drawing
DRAW_DIRECTION_LINE=False
DRAW_TIME_IN_FUTURE_LINE=1

GRAPH_X_LIMITS=[] # 2 NUMBERS
GRAPH_Y_LIMITS=[] # 2 NUMBERS

# (Seconds) This avoids chaos. If None, calculation frames delta time will be calculated in real time. Which will lead to different results for each try
ANIMATION_FIXED_DELTA_TIME=0.0001 # Lower values increases precision and decreases simulation speed

# This will make simulation behind the scenes faster. But keeping the draw rate. If it's too high, pathes might look weird
TIME_WARP=2000