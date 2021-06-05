import pytest

from util.file_io import FileIO
from unittest.mock import patch, mock_open


class TestFileIO:

    def test_write(self):
        open_mock = mock_open()
        with patch("util.file_io.open", open_mock, create=True):
            FileIO.write("/tmp/output.txt", ["test-data"])

        open_mock.assert_called_with("/tmp/output.txt", "w")
        open_mock.return_value.write.assert_called_once_with("test-data")

    def test_read(self):
        open_mock = mock_open()
        with patch("util.file_io.open", open_mock, create=True):
            data = FileIO.read("/tmp/output.txt")

        open_mock.assert_called_with("/tmp/output.txt", "r")