import json
from typing import Iterable


class FileIO:

    @staticmethod
    def read(file_path: str) -> list:
        """
        Reads from the input customer file
        :param file_path: str: path of the input customer file
        :rtype: object: returns customer_details reads from the file
        """
        customer_details = []

        with open(file_path, 'r') as reader:
            for line in reader:
                customer_details.append(json.loads(line))

        return customer_details

    @staticmethod
    def write(file_path: str, data: Iterable[str]) -> None:
        """
        Writes to the output file
        :param data: Iterable[str]: List of strings
        :param file_path: str: path of the output file
        :rtype: None
        """
        with open(file_path, 'w') as writer:
            writer.write('\n'.join(data))
