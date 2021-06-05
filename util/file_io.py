import json


class FileIO:

    @staticmethod
    def read() -> list:
        """

        :rtype: object
        """
        customer_details = []

        with open('../resources/customer.txt', 'r') as reader:
            for line in reader:
                customer_details.append(json.loads(line))

        return customer_details

    @staticmethod
    def write(data) -> None:
        """

        :rtype: None
        """
        with open('../resources/output.txt', 'w') as writer:
            writer.write('\n'.join(data))
