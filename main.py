from app_lib.underground_file_reader import UndergroundFileReader
from app_lib.station import Station
from app_lib.calculator import *
from statistics import *
import os

under = UndergroundFileReader("C:/Users/RPrince/Documents/python-git-class/london_underground/app_lib/london_underground.xlsx")
# new = UndergroundFileReader(os.path.abspath("london_underground.xlsx"))

new_list = list_of_station_class(under.data)

top_weekday_exit = sort_list_by_weekday_exit(new_list)

top_annual_entry_exit = sort_list_by_annual_entry_exit(new_list)

print_top_list_annual_entry_exit(top_weekday_exit, 5)

input()

london_stations = selected_borough(new_list, "City of London")

most_weekday_exit_london = sort_list_by_weekday_exit(london_stations)

print_top_list_weekday_exit(most_weekday_exit_london, 5)

input()

all_weekday_exit = list_of_weekday_exit(new_list)
london_stations_weekday_exit = list_of_weekday_exit(london_stations)

print("Average Weekday Exits From all Stations: " + str(int(mean(all_weekday_exit))))
print("Average Weekday Exits From City of London Stations: " + str(int(mean(london_stations_weekday_exit))))



