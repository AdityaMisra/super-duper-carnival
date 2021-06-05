from typing import List

from dto.customer_details import CustomerDetails
from util.distance_calculator import DistanceCalculator
from util.file_io import FileIO


class InvitationService:
    destination: tuple = (53.339428, -6.257664)  # Dublin, Ireland

    def find_invitees_within_radius(self, range_radius: float = 100.0) -> object:
        """

        :rtype: object
        """

        customer_details = self.get_customer_details()

        nearest_customers = []
        for customer in customer_details:

            origin = (customer.latitude, customer.longitude)

            distance = DistanceCalculator.compute_distance(origin, self.destination)

            if distance < range_radius:
                nearest_customers.append((customer.user_id, customer.name))

        nearest_customers.sort(key=lambda x: x[0])

        # converting user_id into string & joining values of tuple to form a string
        FileIO.write(map(lambda x: ", ".join(map(str, x)), nearest_customers))
        return nearest_customers

    @staticmethod
    def get_customer_details() -> List[CustomerDetails]:
        """

        :rtype: object
        """
        customer_details = FileIO.read()
        return list(map(lambda i: CustomerDetails(**i), customer_details))
