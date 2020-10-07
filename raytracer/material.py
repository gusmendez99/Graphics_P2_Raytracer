from raytracer.utils import Color
from raytracer.math import V3

WHITE = Color(255, 255, 255)


class Light(object):
    def __init__(self, position=V3(0, 0, 0), intensity=1):
        self.position = position
        self.intensity = intensity


class Material(object):
    def __init__(self, diffuse=WHITE, albedo=(1, 0, 0, 0), spec=0, refractive_index=1):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec
        self.refractive_index = refractive_index


class Intersect(object):
    def __init__(self, distance, point, normal):
        self.distance = distance
        self.point = point
        self.normal = normal
