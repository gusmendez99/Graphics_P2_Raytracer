from raytracer.math import sub, dot, length, sum, norm, mul, V3
from raytracer.material import Intersect


class Plane(object):
    def __init__(self, position, normal, material):
        self.position = position
        self.normal = norm(normal)
        self.material = material

    def ray_intersect(self, origin, direction):
        d = dot(direction, self.normal)

        if abs(d) > 0.0001:
            t = dot(self.normal, sub(self.position, origin)) / d
            if t > 0:
                hit = sum(origin, V3(direction.x*t, direction.y*t, direction.z*t))

                return Intersect(distance = t,
                                 point = hit,
                                 normal = self.normal)

        return None
