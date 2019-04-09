from app_lib.underground_file_reader import UndergroundFileReader
from pytest import *

class TestUndergroundFileReader:

    def test_no_file_found(self):
        with raises(FileNotFoundError):
            UndergroundFileReader("no_file.xlsx")