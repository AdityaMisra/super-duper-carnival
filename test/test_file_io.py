import pytest

from util.file_io import FileIO
from unittest.mock import patch, mock_open

class TestFileIO:

    def test_file_read(self):
        open_mock = mock_open()
        with patch("main.open", open_mock, create=True):
            FileIO.write("test-data")

        open_mock.assert_called_with("output.txt", "w")
        open_mock.return_value.write.assert_called_once_with("test-data")
            # assert isinstance(FileIO.read(), list)
