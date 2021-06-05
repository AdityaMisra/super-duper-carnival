import json


class FileIO:

    @staticmethod
    def read(file_path) -> list:
        """

        :rtype: object
        """
        customer_details = []

        with open(file_path, 'r') as reader:
            for line in reader:
                customer_details.append(json.loads(line))

        return customer_details

    @staticmethod
    def write(file_path, data) -> None:
        """

        :rtype: None
        """
        with open(file_path, 'w') as writer:
            writer.write('\n'.join(data))
