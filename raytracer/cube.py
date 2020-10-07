from raytracer.math import V3, sum
from raytracer.material import Intersect
from raytracer.plane import Plane


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
