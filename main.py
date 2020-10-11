from raytracer.ray import Raytracer, GREY
from raytracer.envmap import Envmap
from raytracer.material import Material, Light, AmbientLight
from raytracer.geometry import Sphere, Plane, Cube, Cylinder, Pyramid
from raytracer.utils import Color
from raytracer.math import V3

# Colors & Materials
sky_blue = Color(77,166,255)

ivory = Material(diffuse=Color(255, 255, 200), albedo=(0.6, 0.3, 0.1, 0), spec=50)
rubber = Material(diffuse=Color(80, 0, 0), albedo=(0.9, 0.1, 0, 0, 0), spec=10)
wood = Material(diffuse=Color(56, 24, 2), albedo=(0.9, 0.2, 0, 0.1, 0), spec=150)
mirror = Material(diffuse=Color(255, 255, 255), albedo=(0, 10, 0.8, 0), spec=1425)
leafs = Material(diffuse=Color(0, 102, 0), albedo=(1, 1, 0, 0), spec=50, refractive_index=0)
glass = Material(
    diffuse=Color(150, 180, 200),
    albedo=(0, 0.5, 0.1, 0.8),
    spec=125,
    refractive_index=1.5,
)
water = Material(diffuse=Color(80, 80, 120), albedo=(0, 0.5, 0.1, 0.8), spec=125, refractive_index=1.5)

# Render
render = Raytracer(320, 180) # Test with 448 x 252
#render.envmap = Envmap('./assets/envmap.bmp')
render.light = Light(position=V3(0, 2, 0.2), intensity=1.5)
render.ambient_light = AmbientLight(strength = 0.1)

render.background_color = sky_blue

render.scene = [
    # MOUNTAINS
    Pyramid([V3(-9.5, 0.5, -11), V3(-6.5, 0.5, -11),  V3(-9.8, 0.8, -11.5), V3(-8, 3.4, -11.5), ], wood),
    Pyramid([V3(-6, 0.5, -10),  V3(-4, 0.5, -10), V3(-6.3, 0.7, -10.5), V3(-5, 2, -10),], leafs),
    Pyramid([V3(5, 2, -10),  V3(4.3, 0.7, -10.5), V3(6.3, 0.5, -10),  V3(4, 0.5, -10),  ], leafs),
    Pyramid([V3(8.3, 3.4, -11),  V3(7.1, 0.8, -11.5), V3(9.8, 0.5, -11),  V3(6.8, 0.5, -11),  ], wood),
    
    # LINCOLN MEMORIAL
    # cement bleachers
    Cube(V3(-2, 0.75, -9.25), 0.5, rubber),
    Cube(V3(-1.5, 0.75, -9.25), 0.5, rubber),
    Cube(V3(-1, 0.75, -9.25), 0.5, rubber),
    Cube(V3(-0.5, 0.75, -9.25), 0.5, rubber),
    Cube(V3(0, 0.75, -9.25), 0.5, rubber),
    Cube(V3(0.5, 0.75, -9.25), 0.5, rubber),
    Cube(V3(1, 0.75, -9.25), 0.5, rubber),
    Cube(V3(1.5, 0.75, -9.25), 0.5, rubber),
    Cube(V3(2, 0.75, -9.25), 0.5, rubber),
    # low cement bleachers
    Cube(V3(-2.5, 0.25, -9), 0.5, rubber),
    Cube(V3(-2, 0.25, -9), 0.5, rubber),
    Cube(V3(-1.5, 0.25, -9), 0.5, rubber),
    Cube(V3(-1, 0.25, -9), 0.5, rubber),
    Cube(V3(-0.5, 0.25, -9), 0.5, rubber),
    Cube(V3(0, 0.25, -9), 0.5, rubber),
    Cube(V3(0.5, 0.25, -9), 0.5, rubber),
    Cube(V3(1, 0.25, -9), 0.5, rubber),
    Cube(V3(1.5, 0.25, -9), 0.5, rubber),
    Cube(V3(2, 0.25, -9), 0.5, rubber),
    Cube(V3(2.5, 0.25, -9), 0.5, rubber),
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
    # inside memorial
    Cube(V3(0, 2, -11), 2, rubber),
    Cube(V3(0, 2, -11.2), 4, ivory),
    # mid bar
    Cube(V3(-2, 3, -9.5), 0.5, rubber),
    Cube(V3(-1.5, 3, -9.5), 0.5, rubber),
    Cube(V3(-1, 3, -9.5), 0.5, rubber),
    Cube(V3(-0.5, 3, -9.5), 0.5, rubber),
    Cube(V3(0, 3, -9.5), 0.5, rubber),
    Cube(V3(0.5, 3, -9.5), 0.5, rubber),
    Cube(V3(1, 3, -9.5), 0.5, rubber),
    Cube(V3(1.5, 3, -9.5), 0.5, rubber),
    Cube(V3(2, 3, -9.5), 0.5, rubber),
    # upper bar
    Cube(V3(-1.5, 3.5, -10), 0.5, rubber),
    Cube(V3(-1, 3.5, -10), 0.5, rubber),
    Cube(V3(-0.5, 3.5, -10), 0.5, rubber),
    Cube(V3(0, 3.5, -10), 0.5, rubber),
    Cube(V3(0.5, 3.5, -10), 0.5, rubber),
    Cube(V3(1, 3.5, -10), 0.5, rubber),
    Cube(V3(1.5, 3.5, -10), 0.5, rubber),
    

    # LAKE AND GRASS
    Plane( V3(0, 0, -10), V3(0,1, 0.08), water),
    # sidewalks
    Cube(V3(14, -9.5, -10), 10, rubber),
    Cube(V3(-14, -9.5, -10), 10, rubber),
    # memorial grass
    Cube(V3(-11, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-10.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-10, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-9.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-9, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-8.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-8, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-7.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-7, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-6.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-6, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-5.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-4.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-4, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-3.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-3, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-2.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-2, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-1.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-1, 0.25, -9.25), 0.5, leafs),
    Cube(V3(-0.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(0, 0.25, -9.25), 0.5, leafs),
    Cube(V3(0.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(1, 0.25, -9.25), 0.5, leafs),
    Cube(V3(1.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(2, 0.25, -9.25), 0.5, leafs),
    Cube(V3(2.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(3, 0.25, -9.25), 0.5, leafs),
    Cube(V3(3.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(4, 0.25, -9.25), 0.5, leafs),
    Cube(V3(4.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(5.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(6, 0.25, -9.25), 0.5, leafs),
    Cube(V3(6.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(7, 0.25, -9.25), 0.5, leafs),
    Cube(V3(7.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(8, 0.25, -9.25), 0.5, leafs),
    Cube(V3(8.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(9, 0.25, -9.25), 0.5, leafs),
    Cube(V3(9.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(10, 0.25, -9.25), 0.5, leafs),
    Cube(V3(10.5, 0.25, -9.25), 0.5, leafs),
    Cube(V3(11, 0.25, -9.25), 0.5, leafs),
]



"""
render.scene = [
    Cube(V3(2, -2, -10), 1, rubber),
    Sphere(V3(-1, -0.4, -5), 0.4, ivory),
    Cylinder(1, 0.8, V3(1.2, -0.5, -10), ivory),
    Pyramid([V3(6, -2, -10), V3(4, 1.8, -5), V3(10, -2, -10), V3(4, -1, -7.5)], ivory),
    Plane( V3(-2,-3, -15), V3(1,1,0), glass),
]
"""

render.finish()
