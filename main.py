from london_underground.underground_file_reader import UndergroundFileReader
from london_underground.station import Station
from london_underground.calculator import *
from statistics import *
import os

def story():
    under = UndergroundFileReader(
        "C:/Users/RPrince/Documents/python-git-class/london_underground/london_underground/london_underground.xlsx")
    # new = UndergroundFileReader(os.path.abspath("london_underground.xlsx"))
    # print(os.path.abspath("test_data.xlsx"))

    new_list = list_of_station_class(under.data)

    top_weekday_exit = sort_list_by_weekday_exit(new_list)

    print_top_list_weekday_exit(top_weekday_exit, 5)

    input()

    london_stations = selected_borough(new_list, "City of London")

    top_weekday_exit_london = sort_list_by_weekday_exit(london_stations)

    print_top_list_weekday_exit(top_weekday_exit_london, 5)

    input()

    all_weekday_exit = list_of_weekday_exit(new_list)
    london_stations_weekday_exit = list_of_weekday_exit(london_stations)

    print("Average Weekday Exits From all Stations: " + str(int(mean(all_weekday_exit))))
    print("Average Weekday Exits From City of London Stations: " + str(int(mean(london_stations_weekday_exit))))

    input()

    borough = unique_list_of_boroughs(new_list)

    averages_list = average_per_borough(new_list, borough)

    print_averages(averages_list)

    input()

    top_weekday_entry_london = sort_list_by_weekday_entry(london_stations)

    print_top_list(top_weekday_entry_london, top_weekday_exit_london, 5)

if __name__ == "__main__":
    story()