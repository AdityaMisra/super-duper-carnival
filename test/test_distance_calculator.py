import pytest

from util.distance_calculator import DistanceCalculator


class TestDistanceCalculator:

    def test_distance_calculator(self):
        dc = DistanceCalculator()
        assert int(dc.compute_distance((53.1229599, -6.2705202), (53.339428, -6.257664))) == 24
