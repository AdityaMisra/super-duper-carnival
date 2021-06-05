from math import radians, sin, cos, asin, sqrt, atan2


class DistanceCalculator:

    @staticmethod
    def compute_distance(origin: tuple, destination: tuple) -> float:
        """

        :rtype: object
        """

        lat_origin, lon_origin = origin
        lat_dest, lon_dest = destination
        radius = 6371  # km

        lat_delta = radians(lat_dest - lat_origin)
        lon_delta = radians(lon_dest - lon_origin)

        a = sin(lat_delta / 2) ** 2 + cos(radians(lat_origin)) * cos(radians(lat_dest)) * sin(lon_delta / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = radius * c

        return distance
