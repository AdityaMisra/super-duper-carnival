import pytest

from service.invitation_service import InvitationService


class TestInvitationService:

    def test_get_customer_details(self):
        pass

    def test_get_customers_within_radius(self):
        assert isinstance(InvitationService._get_customers_within_radius(), list)
