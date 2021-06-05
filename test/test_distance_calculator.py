import pytest

from util.distance_calculator import DistanceCalculator


class TestDistanceCalculator:

    def test_gift_card_service(self):
        dc = DistanceCalculator()

        assert int(dc.compute_distance((53.1229599, -6.2705202), (53.339428, -6.257664))) == 24
