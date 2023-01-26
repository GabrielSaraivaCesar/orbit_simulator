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
    "SIMPLE_ORBIT_3": [
        Planet(x=0, y=200000, mass=0, size=50, v_x=20000),
        Planet(x=0, y=405400, mass=0, size=50, v_x=20000, z=200000),
        Planet(x=0, y=0, mass=0, size=50, v_x=20000, z=405400),
        Planet(x=0, y=0, mass=5.972*10**24, size=500, is_fixed=True),
    ],

    "HIGH_INFLUENCES": [
        Planet(x=1000, y=4000, mass=10*10**16, size=50, v_x=100),
        Planet(x=0, y=3000, mass=2*10**15, size=50, v_x=200),
        Planet(x=0, y=0, mass=2*10**18, size=200, is_fixed=True),
    ],

    "SYNCHRONOUS_ORBITS": [
        Planet(x=0, y=600, mass=0, size=50, v_x=100),
        Planet(x=0, y=-600, mass=0, size=50, v_x=-100),
        Planet(x=600, y=0, mass=0, size=50, v_y=-100),
        Planet(x=-600, y=0, mass=0, size=50, v_y=100),
        Planet(x=0, y=0, mass=1*10**17, size=200, is_fixed=True),
    ],
    
    "KERBOL_SYSTEM": [
        Planet(x=0, y=13_599_840_256, mass=0, size=6371/100, v_x=-9285, color="#75bd39"), # Earth
        Planet(x=0, y=0, mass=1.7565459*(10**28), size=696340/200, is_fixed=True, color="#fc9300"), # Sun
    ],
}


def get_preset_by_name(name:str):
    return presets_object[name.upper()]


def is_preset_3d(preset):
    is_3d = False
    for planet in preset:
        if planet.z is not None:
            is_3d = True
            break
    return is_3d

def normalize_3d_preset(preset):
    for planet in preset:
        if planet.z is None:
            planet.z = 0
        if planet.v_z is None:
            planet.v_z = 0