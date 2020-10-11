from raytracer.ray import Raytracer, GREY
from raytracer.envmap import Envmap
from raytracer.material import Material, Light, AmbientLight, Texture
from raytracer.geometry import Sphere, Plane, Cube, Cylinder, Pyramid
from raytracer.utils import Color
from raytracer.math import V3

# Colors & Materials
SKY_BLUE = Color(77,166,255)
YELLOW = Color(255, 255, 200)
BROWN = Color(98, 42, 4)
GREEN = Color(77, 102, 0)
LIGHT_PURPLE = Color(80, 80, 120)
BABY_BLUE = Color(150, 180, 200)

ivory = Material(diffuse=YELLOW, albedo=(0.6, 0.3, 0.1, 0), spec=50)
wood = Material(diffuse=BROWN, albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
leaf = Material(diffuse=GREEN, albedo=(1, 1, 0, 0), spec=50, refractive_index=0)
water = Material(diffuse=LIGHT_PURPLE, albedo=(0, 0.5, 0.1, 0.8), spec=125, refractive_index=1.5)
glass = Material(
    diffuse=BABY_BLUE,
    albedo=(0, 0.5, 0.1, 0.8),
    spec=125,
    refractive_index=1.5,
)
cement = Material(texture=Texture('./assets/cement.bmp'))
grass = Material(texture=Texture('./assets/grass.bmp'))

# Just for get run time
import time
start_time = time.time() 

# Render
render = Raytracer(768, 432)
render.envmap = Envmap('./assets/sunset.bmp')
render.light = Light(position=V3(0, 2, 0.2), intensity=1.5)
render.ambient_light = AmbientLight(strength = 0.1)
render.background_color = SKY_BLUE

render.scene = [
    # MOUNTAINS
    Pyramid([V3(-9.5, 0.5, -11), V3(-6.5, 0.5, -11),  V3(-9.8, 0.8, -11.5), V3(-8, 3.4, -11.5), ], wood),
    Pyramid([V3(-6, 0.5, -10),  V3(-4, 0.5, -10), V3(-6.3, 0.7, -10.5), V3(-5, 2, -10),], leaf),
    Pyramid([V3(5, 2, -10),  V3(4.3, 0.7, -10.5), V3(6.3, 0.5, -10),  V3(4, 0.5, -10),  ], leaf),
    Pyramid([V3(8.3, 3.4, -11),  V3(7.1, 0.8, -11.5), V3(9.8, 0.5, -11),  V3(6.8, 0.5, -11),  ], wood),
    
    # LINCOLN MEMORIAL
    # cement bleachers
    Cube(V3(-2, 0.75, -9.25), 0.5, cement),
    Cube(V3(-1.5, 0.75, -9.25), 0.5, cement),
    Cube(V3(-1, 0.75, -9.25), 0.5, cement),
    Cube(V3(-0.5, 0.75, -9.25), 0.5, cement),
    Cube(V3(0, 0.75, -9.25), 0.5, cement),
    Cube(V3(0.5, 0.75, -9.25), 0.5, cement),
    Cube(V3(1, 0.75, -9.25), 0.5, cement),
    Cube(V3(1.5, 0.75, -9.25), 0.5, cement),
    Cube(V3(2, 0.75, -9.25), 0.5, cement),
    # low cement bleachers
    Cube(V3(-2.5, 0.25, -9), 0.5, cement),
    Cube(V3(-2, 0.25, -9), 0.5, cement),
    Cube(V3(-1.5, 0.25, -9), 0.5, cement),
    Cube(V3(-1, 0.25, -9), 0.5, cement),
    Cube(V3(-0.5, 0.25, -9), 0.5, cement),
    Cube(V3(0, 0.25, -9), 0.5, cement),
    Cube(V3(0.5, 0.25, -9), 0.5, cement),
    Cube(V3(1, 0.25, -9), 0.5, cement),
    Cube(V3(1.5, 0.25, -9), 0.5, cement),
    Cube(V3(2, 0.25, -9), 0.5, cement),
    Cube(V3(2.5, 0.25, -9), 0.5, cement),
    # inside memorial
    Cube(V3(-1, 2, -11.5), 2, cement),
    Cube(V3(1, 2, -11.5), 2, cement),
    Cube(V3(0, 2, -11), 2, ivory),
    # columns
    Cylinder(0.15, 1.8, V3(-2, 1, -10), ivory),
    Cylinder(0.15, 1.8, V3(-1.5, 1, -10), ivory),
    Cylinder(0.15, 1.8, V3(-1, 1, -10), ivory),
    Cylinder(0.15, 1.8, V3(-0.5, 1, -10), ivory),
    Cylinder(0.15, 1.8, V3(0, 1, -10), ivory),
    Cylinder(0.15, 1.8, V3(0.5, 1, -10), ivory),
    Cylinder(0.15, 1.8, V3(1, 1, -10), ivory),
    Cylinder(0.15, 1.8, V3(1.5, 1, -10), ivory),
    Cylinder(0.15, 1.8, V3(2, 1, -10), ivory),
    # mid bar
    Cube(V3(-2, 3, -9.5), 0.5, cement),
    Cube(V3(-1.5, 3, -9.5), 0.5, cement),
    Cube(V3(-1, 3, -9.5), 0.5, cement),
    Cube(V3(-0.5, 3, -9.5), 0.5, cement),
    Cube(V3(0, 3, -9.5), 0.5, cement),
    Cube(V3(0.5, 3, -9.5), 0.5, cement),
    Cube(V3(1, 3, -9.5), 0.5, cement),
    Cube(V3(1.5, 3, -9.5), 0.5, cement),
    Cube(V3(2, 3, -9.5), 0.5, cement),
    # upper bar
    Cube(V3(-1.5, 3.5, -10), 0.5, cement),
    Cube(V3(-1, 3.5, -10), 0.5, cement),
    Cube(V3(-0.5, 3.5, -10), 0.5, cement),
    Cube(V3(0, 3.5, -10), 0.5, cement),
    Cube(V3(0.5, 3.5, -10), 0.5, cement),
    Cube(V3(1, 3.5, -10), 0.5, cement),
    Cube(V3(1.5, 3.5, -10), 0.5, cement),

    # LAKE AND GRASS
    Plane( V3(0, 0, -10), V3(0,1, 0.05), water),
    # memorial grass
    Cube(V3(-11, 0.25, -9.25), 0.5, grass),
    Cube(V3(-10.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(-10, 0.25, -9.25), 0.5, grass),
    Cube(V3(-9.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(-9, 0.25, -9.25), 0.5, grass),
    Cube(V3(-8.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(-8, 0.25, -9.25), 0.5, grass),
    Cube(V3(-7.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(-7, 0.25, -9.25), 0.5, grass),
    Cube(V3(-6.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(-6, 0.25, -9.25), 0.5, grass),
    Cube(V3(-5.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(-5, 0.25, -9.25), 0.5, grass),
    Cube(V3(-4.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(-4, 0.25, -9.25), 0.5, grass),
    Cube(V3(-3.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(-3, 0.25, -9.25), 0.5, grass),
    Cube(V3(-2.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(-2, 0.25, -9.25), 0.5, grass),
    Cube(V3(-1.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(-1, 0.25, -9.25), 0.5, grass),
    Cube(V3(-0.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(0, 0.25, -9.25), 0.5, grass),
    Cube(V3(0.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(1, 0.25, -9.25), 0.5, grass),
    Cube(V3(1.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(2, 0.25, -9.25), 0.5, grass),
    Cube(V3(2.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(3, 0.25, -9.25), 0.5, grass),
    Cube(V3(3.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(4, 0.25, -9.25), 0.5, grass),
    Cube(V3(4.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(5, 0.25, -9.25), 0.5, grass),
    Cube(V3(5.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(6, 0.25, -9.25), 0.5, grass),
    Cube(V3(6.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(7, 0.25, -9.25), 0.5, grass),
    Cube(V3(7.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(8, 0.25, -9.25), 0.5, grass),
    Cube(V3(8.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(9, 0.25, -9.25), 0.5, grass),
    Cube(V3(9.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(10, 0.25, -9.25), 0.5, grass),
    Cube(V3(10.5, 0.25, -9.25), 0.5, grass),
    Cube(V3(11, 0.25, -9.25), 0.5, grass), 
    # sidewalks
    Cube(V3(13, -9.5, -9), 10, grass),
    Cube(V3(-13, -9.5, -9), 10, grass),
    Plane( V3(0, 0, -10), V3(0,1, 0.05), water),
    Sphere(V3(5, 0.15, -7), 0.2, glass),
    Sphere(V3(-5, 0.15, -7), 0.2, glass),
]

render.finish()
print("--- Render done in %s seconds ---" % (time.time() - start_time))
