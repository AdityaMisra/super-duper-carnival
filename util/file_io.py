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

        if not file_path:
            raise Exception("Invalid file path for reading the input")

        customer_details = []

        try:
            with open(file_path, 'r') as reader:
                for line in reader:
                    customer_details.append(json.loads(line))
        except Exception as e:
            raise Exception("Error while reading from the input file")

        return customer_details

    @staticmethod
    def write(file_path: str, data: Iterable[str]) -> None:
        """
        Writes to the output file
        :param data: Iterable[str]: List of strings
        :param file_path: str: path of the output file
        :rtype: None
        """

        if not file_path:
            raise Exception("Invalid file path for writing the output")

        try:
            with open(file_path, 'w') as writer:
                writer.write('\n'.join(data))
        except Exception as e:
            raise Exception("Error while writing to the output file")
