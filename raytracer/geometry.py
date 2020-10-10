"""
	Credits to @tobycyanide for geometry ray_intersect ideas
	Repo: https://github.com/tobycyanide/pytracer
"""

from raytracer.math import *
from raytracer.material import Intersect
from math import sqrt, inf


class Plane(object):
    """
    Creates a new Plane model    
    """
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
    """
    Creates a new Cube model    
    """
    def __init__(self, position, size, material):
        self.position = position
        self.size = size
        self.material = material
        mid_size = size / 2

        self.planes = [
            Plane(sum(position, V3(mid_size, 0, 0)), V3(1, 0, 0), material),
            Plane(sum(position, V3(-mid_size, 0, 0)), V3(-1, 0, 0), material),
            Plane(sum(position, V3(0, mid_size, 0)), V3(0, 1, 0), material),
            Plane(sum(position, V3(0, -mid_size, 0)), V3(0, -1, 0), material),
            Plane(sum(position, V3(0, 0, mid_size)), V3(0, 0, 1), material),
            Plane(sum(position, V3(0, 0, -mid_size)), V3(0, 0, -1), material)
        ]
        

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
    """
    Creates a new Sphere model    
    """
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
    """
    Creates a new Cylinder model    
    """
    def __init__(self, radius, height, center, material):
        self.radius = radius
        self.height = height
        self.closed = False
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

    def check_cap(self, origin, direction, t):
        x = origin.x + t * direction.x
        z = origin.z + t * direction.z
        return (x ** 2 + z ** 2) <= abs(self.radius)

    def intersect_caps(self, origin, direction):
        if self.closed == False or abs(direction.y) < EPSILON:
            return None

        t_lower = (self.center.y - origin.y) / direction.y
        if self.check_cap(origin, direction, t_lower):
            hit = sum(origin, mul(direction, t_lower))
            normal = norm(sub(hit, self.center))
            return Intersect(distance=t_lower, point=hit, normal=normal)

        t_upper = ((self.center.y + self.height) - origin.y) / direction.y
        if self.check_cap(origin, direction, t_upper):
            hit = sum(origin, mul(direction, t_upper))
            normal = norm(sub(hit, self.center))
            return Intersect(distance=t_upper, point=hit, normal=normal)

        return None


class Triangle(object):
    """
    Creates a new Triangle model    
    """
    def __init__(self, vertices, material):
        self.vertices = vertices
        self.material = material

    def ray_intersect(self, origin, direction):
        v0, v1, v2 = self.vertices
        normal = norm(cross(sub(v1, v0), sub(v2, v0)))
        determinant = dot(normal, direction)

        if abs(determinant) < EPSILON:
            return None

        distance = dot(normal, v0)
        t = (dot(normal, origin) + distance) / determinant

        if t < 0:
            return None

        point = sum(origin, mul(direction, t))
        u, v, w = barycentric(v0, v1, v2, point)

        if w < 0 or v < 0 or u < 0:  # 0 is actually a valid value! (it is on the edge)
            return None
        else:
            return Intersect(distance=distance, point=point, normal=norm(normal))

        # Checks determinant with all edges
        normal = norm(cross(sub(v1, v0), sub(point, v0)))
        determinant = dot(normal, direction)

        if abs(determinant) < EPSILON:
            return None

        normal = norm(cross(sub(v2, v1), sub(point, v1)))
        determinant = dot(normal, direction)

        if abs(determinant) < EPSILON:
            return None

        normal = norm(cross(sub(v0, v2), sub(point, v2)))
        determinant = dot(normal, direction)

        if abs(determinant) < EPSILON:
            return None

        return Intersect(distance=(t / determinant), point=point, normal=norm(normal))


class Pyramid(object):
    """
    Creates a new Pyramid model (made of 4 triangles)
    """

    def __init__(self, vertices, material):
        self.sides = self.generate_sides(vertices, material)
        self.material = material

    def generate_sides(self, vertices, material):
        if len(vertices) != 4:
            return [None, None, None, None]

        v0, v1, v2, v3 = vertices
        sides = [
            Triangle([v0, v3, v2], material),
            Triangle([v0, v1, v2], material),
            Triangle([v1, v3, v2], material),
            Triangle([v0, v1, v3], material),
        ]
        return sides

    def ray_intersect(self, origin, direction):
        t = float("inf")
        intersect = None

        for triangle in self.sides:
            local_intersect = triangle.ray_intersect(origin, direction)
            if local_intersect is not None:
                if local_intersect.distance < t:
                    t = local_intersect.distance
                    intersect = local_intersect

        if intersect is None:
            return None

        return Intersect(
            distance=intersect.distance, point=intersect.point, normal=intersect.normal
        )
