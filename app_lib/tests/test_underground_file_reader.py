from app_lib.underground_file_reader import UndergroundFileReader
from pytest import *
import os


class TestUndergroundFileReader:
    # test_reader = UndergroundFileReader(os.path.abspath("test_data.xlsx"))

    def test_no_file_found(self):
        with raises(FileNotFoundError, match= "no file found"):
            UndergroundFileReader("no_file.xlsx")

    # def test_top_stations(self):
    #     assert self.test_reader.top_stations(weekday_entry, 1) == "test station 3"
