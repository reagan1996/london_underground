# from london_underground.underground_file_reader import UndergroundFileReader
from pytest import *
import london_underground
from london_underground.calculator import *
import os


class TestUndergroundFileReader:
    test_reader = UndergroundFileReader(os.path.normpath(os.path.join(os.getcwd(), "test_data.xlsx")))
        # os.path.abspath("test_data.xlsx"))
    test_data = list_of_station_class(test_reader.data)

    def test_no_file_found(self):
        with raises(FileNotFoundError, match= "no file found"):
            UndergroundFileReader("no_file.xlsx")

    def test_select_borough(self):
         assert selected_borough(self.test_data, "Brent")[0].station_name == "test station 3"

    def test_top_weekday_entry(self):
        assert sort_list_by_weekday_entry(self.test_data)[0].station_name == "test station 2"

    def test_bottom_weekday_exit(self):
        assert sort_list_by_weekday_exit(self.test_data,False)[0].station_name == "test station 1"

    def test_average_per_borough(self):
        borough = unique_list_of_boroughs(self.test_data)
        assert average_per_borough(self.test_data,borough) == [["Brent", 10], ["City of London", 7]]

