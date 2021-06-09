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

    def test_write_with_exception(self):
        with pytest.raises(Exception):
            FileIO.write(None, [])

    def test_read(self):
        read_data = '{"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"}'
        open_mock = mock_open(read_data=read_data)

        with patch("util.file_io.open", open_mock, create=True):
            data = FileIO.read("/tmp/customer.txt")

        open_mock.assert_called_with("/tmp/customer.txt", "r")
        assert len(data) == 1

    def test_read_with_exception(self):
        with pytest.raises(Exception):
            FileIO.read(None)
