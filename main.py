from app_lib.underground_file_reader import UndergroundFileReader
from app_lib.station import Station
from app_lib.calculator import *
import os

under = UndergroundFileReader("C:/Users/RPrince/Documents/python-git-class/london_underground/app_lib/london_underground.xlsx")
# new = UndergroundFileReader(os.path.abspath("london_underground.xlsx"))

new_list = list_of_station_class(under.data)

top_weekday_exit = sort_list_by_weekday_entry(new_list)

top_annual_entry_exit = sort_list_by_annual_entry_exit(new_list)

print_top_list_annual_entry_exit(top_annual_entry_exit, 5)