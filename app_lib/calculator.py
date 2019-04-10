from app_lib.underground_file_reader import UndergroundFileReader
from app_lib.station import Station
import os

def list_of_station_class(data):
    list_of_stations = []
    for row in data:
        list_of_stations.append(Station(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
    return list_of_stations

def selected_borough(list_of_data, borough):
    new_list = []
    for row in list_of_data:
        if row.borough == borough:
            new_list.append(row)
    return new_list

def sort_list_by_weekday_entry(list_of_data, desc= True):
    return sorted(list_of_data, key=lambda x: x.weekday_entry, reverse= desc)

def sort_list_by_saturday_entry(list_of_data, desc= True):
    return sorted(list_of_data, key=lambda x: x.saturday_entry, reverse= desc)

def sort_list_by_sunday_entry(list_of_data, desc= True):
    return sorted(list_of_data, key=lambda x: x.sunday_entry, reverse= desc)

def sort_list_by_weekday_exit(list_of_data, desc= True):
    return sorted(list_of_data, key=lambda x: x.weekday_exit, reverse= desc)

def sort_list_by_saturday_exit(list_of_data, desc= True):
    return sorted(list_of_data, key=lambda x: x.saturday_exit, reverse= desc)

def sort_list_by_sunday_exit(list_of_data, desc= True):
    return sorted(list_of_data, key=lambda x: x.sunday_exit, reverse= desc)

def sort_list_by_annual_entry_exit(list_of_data, desc= True):
    return sorted(list_of_data, key=lambda x: x.annual_entry_exit, reverse= desc)

def print_top_list(sorted_list, number_of_results):
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print(sorted_list[0].return_titles())
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    index = 1
    for station in sorted_list[0:number_of_results]:
        print(index, ". ")
        print(station.return_details())
        index += 1

def print_top_list_weekday_exit(sorted_list, number_of_results):
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print(sorted_list[0].return_weekday_exit_title())
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    index = 1
    for station in sorted_list[0:number_of_results]:
        print(index, ". ")
        print(station.return_weekday_exit_details())
        index += 1

def print_top_list_annual_entry_exit(sorted_list, number_of_results):
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print(sorted_list[0].return_annual_entry_exit_title())
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    index = 1
    for station in sorted_list[0:number_of_results]:
        print(index, ". ")
        print(station.return_annual_entry_exit_details())
        index += 1

