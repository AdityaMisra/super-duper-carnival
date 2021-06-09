from typing import List, Iterable

from dto.customer_details import CustomerDetails
from util.distance_calculator import DistanceCalculator
from util.file_io import FileIO


class InvitationService:
    destination: tuple = (53.339428, -6.257664)  # Dublin, Ireland

    def __init__(self, input_file_path: str, output_file_path: str) -> None:
        """
        Constructor of InvitationService
        :param input_file_path: file path of the customer file
        :param output_file_path: path of the output file
        """

        super().__init__()
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def find_customers_within_radius(self, radius_range: float = 100.0) -> None:
        """
        This method parses through the input file of customers and writes the details of valid customers in the output file.
        Valid customers are those whose home location is within the radius_range of the Dublin office location.
        :param radius_range: float: default value is 100.0 km
        :rtype: None: write the output in the `output_file_path`
        """

        customer_details = self.get_customer_details()

        nearest_customers = self._get_customers_within_radius(customer_details, radius_range)

        # converting user_id into string & joining values of tuple to form a string
        nearest_customers = map(lambda x: ", ".join(map(str, x)), nearest_customers)

        self.write_to_output_file(nearest_customers)

        return None

    def _get_customers_within_radius(self, customer_details: List[CustomerDetails], radius_range: float) -> list:
        """
        Get valid customers whose home location is within the radius_range of the Dublin office location.
        :type radius_range: float
        :type customer_details: List[CustomerDetails]
        :rtype: list: valid list of customers
        """

        nearest_customers = []
        for customer in customer_details:

            origin = (customer.latitude, customer.longitude)

            distance = DistanceCalculator.compute_distance(origin, self.destination)

            if distance <= radius_range:
                nearest_customers.append((customer.user_id, customer.name))

        nearest_customers.sort(key=lambda x: x[0])

        return nearest_customers

    def write_to_output_file(self, nearest_customers: Iterable[str]) -> None:
        """
        Writes the list of customers to the outpout file.
        :param nearest_customers: Iterable[str]: list of customers whose location is within the radius of the Dublin office
        :rtype: None:
        """

        return FileIO.write(self.output_file_path, nearest_customers)

    def get_customer_details(self) -> List[CustomerDetails]:
        """
        Reads the input customer file, parse it & return a list of CustomerDetails
        :rtype: List[CustomerDetails]
        """

        customer_details = FileIO.read(self.input_file_path)
        return list(map(lambda i: CustomerDetails(**i), customer_details))
