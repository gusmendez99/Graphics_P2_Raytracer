"""
	Credits to @tobycyanide for geometry ray_intersect ideas
	Repo: https://github.com/tobycyanide/pytracer
"""

from raytracer.math import (
    sub,
    dot,
    length,
    sum,
    norm,
    mul,
    V3,
    barycentric,
    cross,
    EPSILON,
)
from raytracer.material import Intersect
from math import sqrt, inf


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
                hit = sum(origin, V3(direction.x * t, direction.y * t, direction.z * t))

                return Intersect(distance=t, point=hit, normal=self.normal)

        return None


class Cube(object):
    def __init__(self, position, size, material):
        self.position = position
        self.size = size
        self.material = material
        self.planes = []

        mid_size = size / 2

        self.planes.append(
            Plane(sum(position, V3(mid_size, 0, 0)), V3(1, 0, 0), material)
        )
        self.planes.append(
            Plane(sum(position, V3(-mid_size, 0, 0)), V3(-1, 0, 0), material)
        )

        self.planes.append(
            Plane(sum(position, V3(0, mid_size, 0)), V3(0, 1, 0), material)
        )
        self.planes.append(
            Plane(sum(position, V3(0, -mid_size, 0)), V3(0, -1, 0), material)
        )

        self.planes.append(
            Plane(sum(position, V3(0, 0, mid_size)), V3(0, 0, 1), material)
        )
        self.planes.append(
            Plane(sum(position, V3(0, 0, -mid_size)), V3(0, 0, -1), material)
        )

    def ray_intersect(self, origin, direction):
        epsilon = 0.001

        min_bounds = [0, 0, 0]
        max_bounds = [0, 0, 0]

        for i in range(3):
            min_bounds[i] = self.position[i] - (epsilon + self.size / 2)
            max_bounds[i] = self.position[i] + (epsilon + self.size / 2)

        t = float("inf")
        intersect = None

        for plane in self.planes:
            plane_intersection = plane.ray_intersect(origin, direction)

            if plane_intersection is not None:
                if (
                    plane_intersection.point[0] >= min_bounds[0]
                    and plane_intersection.point[0] <= max_bounds[0]
                ):
                    if (
                        plane_intersection.point[1] >= min_bounds[1]
                        and plane_intersection.point[1] <= max_bounds[1]
                    ):
                        if (
                            plane_intersection.point[2] >= min_bounds[2]
                            and plane_intersection.point[2] <= max_bounds[2]
                        ):
                            if plane_intersection.distance < t:
                                t = plane_intersection.distance
                                intersect = plane_intersection

        if intersect is None:
            return None

        return Intersect(
            distance=intersect.distance, point=intersect.point, normal=intersect.normal
        )


class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, origin, direction):
        L = sub(self.center, origin)
        tca = dot(L, direction)
        l = length(L)
        d2 = l ** 2 - tca ** 2
        if d2 > self.radius ** 2:
            return None
        thc = (self.radius ** 2 - d2) ** 1 / 2
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None

        hit = sum(origin, mul(direction, t0))
        normal = norm(sub(hit, self.center))

        return Intersect(distance=t0, point=hit, normal=normal)


class Cylinder(object):
    def __init__(self, radius, height, center, material):
        self.radius = radius
        self.height = height
        self.closed = True
        self.center = center
        self.material = material

    def ray_intersect(self, origin, direction):
        a = direction.x ** 2 + direction.z ** 2
        if abs(a) < EPSILON:
            return None

        b = 2 * (
            direction.x * (origin.x - self.center.x)
            + direction.z * (origin.z - self.center.z)
        )
        c = (
            (origin.x - self.center.x) ** 2
            + (origin.z - self.center.z) ** 2
            - (self.radius ** 2)
        )

        discriminant = b ** 2 - 4 * (a * c)

        if discriminant < 0.0:
            return None

        t0 = (-b - sqrt(discriminant)) / (2 * a)
        t1 = (-b + sqrt(discriminant)) / (2 * a)

        if t0 > t1:
            t0, t1, t1, t0

        y0 = origin.y + t0 * direction.y
        if self.center.y < y0 and y0 <= (self.center.y + self.height):
            hit = sum(origin, mul(direction, t0))
            normal = norm(sub(hit, self.center))
            return Intersect(distance=t0, point=hit, normal=normal)

        y1 = origin.y + t1 * direction.y
        if self.center.y < y1 and y1 <= (self.center.y + self.height):
            hit = sum(origin, mul(direction, t1))
            normal = norm(sub(hit, self.center))
            return Intersect(distance=t1, point=hit, normal=normal)

        return self.intersect_caps(origin, direction)

    def check_cap(self, origin, direction, t, radius):
        x = origin.x + t * direction.x
        z = origin.z + t * direction.z
        return (x ** 2 + z ** 2) <= abs(radius)

    def intersect_caps(self, origin, direction):
        if self.closed == False or abs(direction.y) < EPSILON:
            return None

        t_lower = ((self.center.y - self.height) - origin.y) / direction.y
        if self.check_cap(origin, direction, t_lower, 1):
            hit = sum(origin, mul(direction, t_lower))
            normal = norm(sub(hit, self.center))
            return Intersect(distance=t_lower, point=hit, normal=normal)

        t_upper = ((self.center.y + self.height) - origin.y) / direction.y
        if self.check_cap(origin, direction, t_upper, 1):
            hit = sum(origin, mul(direction, t_upper))
            normal = norm(sub(hit, self.center))
            return Intersect(distance=t_upper, point=hit, normal=normal)
