from app_lib.underground_file_reader import UndergroundFileReader
from pytest import *
from app_lib.calculator import *


class TestUndergroundFileReader:
    test_reader = UndergroundFileReader(os.path.abspath("test_data.xlsx"))
    test_data = list_of_station_class(test_reader.data)

    def test_no_file_found(self):
        with raises(FileNotFoundError, match= "no file found"):
            UndergroundFileReader("no_file.xlsx")

    def test_select_borough(self):
         assert selected_borough(self.test_data, "Brent")[0].station_name == "test station 3"

    def test_top_weekday_entry(self):
        assert sort_list_by_weekday_entry(self.test_data)[0].station_name == "test station 2"

    def test_bottom_annual_entry_exit(self):#
        assert sort_list_by_annual_entry_exit(self.test_data,False)[0].station_name == "test station 1"