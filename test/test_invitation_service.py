from unittest.mock import MagicMock

import pytest

from dto.customer_details import CustomerDetails
from service.invitation_service import InvitationService
from util.file_io import FileIO


class TestInvitationService:

    def test_get_customers_within_radius_with_empty_input(self):
        customer_details = []
        radius_range = 100.0

        invitationService = InvitationService("resources/customer.txt", "resources/output.txt")
        assert len(invitationService._get_customers_within_radius(customer_details, radius_range)) == 0

    def test_get_customers_within_radius(self):
        customer_details = [CustomerDetails(latitude=51.92893, longitude=-10.27699, name='Alice Cahill', user_id=1),
                            CustomerDetails(latitude=51.8856167, longitude=-10.4240951, name='Ian McArdle', user_id=2),
                            CustomerDetails(latitude=52.3191841, longitude=-8.5072391, name='Jack Enright', user_id=3),
                            CustomerDetails(latitude=53.4692815, longitude=-9.436036, name='Frank Kehoe', user_id=7),
                            CustomerDetails(latitude=54.0894797, longitude=-6.18671, name='Eoin Ahearn', user_id=8),
                            CustomerDetails(latitude=54.1225, longitude=-8.143333, name='Enid Gallagher', user_id=27),
                            CustomerDetails(latitude=53.1229599, longitude=-6.2705202, name='Theresa Enright',
                                            user_id=6),
                            CustomerDetails(latitude=52.2559432, longitude=-7.1048927, name='Jack Dempsey', user_id=9),
                            CustomerDetails(latitude=53.2451022, longitude=-6.238335, name='Ian Kehoe', user_id=4),
                            CustomerDetails(latitude=53.1302756, longitude=-6.2397222, name='Nora Dempsey', user_id=5)]

        radius_range = 100.0

        invitationService = InvitationService("resources/customer.txt", "resources/output.txt")
        assert len(invitationService._get_customers_within_radius(customer_details, radius_range)) == 4

    def test_find_customers_within_radius_with_empty_list(self):
        invitationService = InvitationService("resources/customer.txt", "resources/output.txt")
        invitationService.get_customer_details = MagicMock(return_value=[])
        invitationService._get_customers_within_radius = MagicMock(return_value=[])
        invitationService.write_to_output_file = MagicMock(return_value=None)

        radius_range = 100.0

        assert invitationService.find_customers_within_radius(radius_range) is None

    def test_find_customers_within_radius(self):
        customer_details = [CustomerDetails(latitude=52.2559432, longitude=-7.1048927, name='Jack Dempsey', user_id=9),
                            CustomerDetails(latitude=53.2451022, longitude=-6.238335, name='Ian Kehoe', user_id=4),
                            CustomerDetails(latitude=53.1302756, longitude=-6.2397222, name='Nora Dempsey', user_id=5)]

        invitationService = InvitationService("resources/customer.txt", "resources/output.txt")
        invitationService.get_customer_details = MagicMock(return_value=customer_details)
        invitationService._get_customers_within_radius = MagicMock(return_value=[(4, 'Ian Kehoe'), (5, 'Nora Dempsey')])
        invitationService.write_to_output_file = MagicMock(return_value=None)

        radius_range = 100.0

        assert invitationService.find_customers_within_radius(radius_range) is None

    def test_write_to_output_file(self):
        FileIO.write = MagicMock(return_value=None)

        nearest_customers = ['4, Ian Kehoe', '5, Nora Dempsey']

        invitationService = InvitationService("resources/customer.txt", "resources/output.txt")
        invitationService.write_to_output_file(nearest_customers)

        FileIO.write.assert_called_with("resources/output.txt", nearest_customers)

    def test_get_customer_details(self):
        customer_details = [
            {
                "latitude": 52.2559432,
                "longitude": -7.1048927,
                "name": "Jack Dempsey",
                "user_id": 9
            },
            {
                "latitude": 53.2451022,
                "longitude": -6.238335,
                "name": "Ian Kehoe",
                "user_id": 4
            },
            {
                "latitude": 53.1302756,
                "longitude": -6.2397222,
                "name": "Nora Dempsey",
                "user_id": 5
            }
        ]

        FileIO.read = MagicMock(return_value=customer_details)

        invitationService = InvitationService("resources/customer.txt", "resources/output.txt")

        assert isinstance(invitationService.get_customer_details()[0], CustomerDetails)
        assert len(invitationService.get_customer_details()) == 3
