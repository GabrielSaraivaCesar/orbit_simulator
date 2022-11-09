from src.elements import Planet

presets_object = {
    "SIMPLE_ORBIT": [
        Planet(x=0, y=405400, mass=0, size=50, v_x=20000),
        Planet(x=0, y=0, mass=5.972*10**24, size=500, is_fixed=True),
    ],
    "SIMPLE_ORBIT_2": [
        Planet(x=0, y=200000, mass=0, size=50, v_x=20000),
        Planet(x=0, y=405400, mass=0, size=50, v_x=20000),
        Planet(x=0, y=0, mass=5.972*10**24, size=500, is_fixed=True),
    ],

    "HIGH_INFLUENCES": [
        Planet(x=0, y=400, mass=10*10**14, size=50, v_x=100),
        Planet(x=0, y=300, mass=2*10**14, size=50, v_x=100),
        Planet(x=0, y=0, mass=2*10**17, size=200, is_fixed=True),
    ],

    "SYNCHRONOUS_ORBITS": [
        Planet(x=0, y=600, mass=0, size=50, v_x=100),
        Planet(x=0, y=-600, mass=0, size=50, v_x=-100),
        Planet(x=600, y=0, mass=0, size=50, v_y=-100),
        Planet(x=-600, y=0, mass=0, size=50, v_y=100),
        Planet(x=0, y=0, mass=1*10**17, size=200, is_fixed=True),
    ],
    
    "SOLAR_SYSTEM": [
        Planet(x=0, y=740.99*1000000, mass=1.898 * 10**27, size=100, v_x=47052*7), # Jupiter
        Planet(x=0, y=225.2*1000000, mass=6.39 * 10**23, size=50, v_x=86677.2*7), # Mars
        Planet(x=0, y=148.19*1000000, mass=5.972 * 10**24, size=50, v_x=108000*7), # Earth
        Planet(x=0, y=108.4*1000000, mass=4.86 * 10**24, size=50, v_x=126072*7), # Venus
        Planet(x=0, y=67.459*1000000, mass=3.285 * 10**23, size=50, v_x=169200*7), # Mercury
        Planet(x=0, y=0, mass=1.989 * 10**30, size=200, is_fixed=True), # sun
    ],
}


def get_preset_by_name(name):
    return presets_object[name]