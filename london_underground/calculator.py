from london_underground.station import Station
from london_underground.underground_file_reader import UndergroundFileReader


# Create a list of Station class object from a list of lists
def list_of_station_class(data):
    list_of_stations = []
    for row in data:
        list_of_stations.append(Station(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
    return list_of_stations

# Create a list of stations from a given borough (must input list of stations and borough)
def selected_borough(list_of_data, borough):
    new_list = []
    for row in list_of_data:
        if row.borough == borough:
            new_list.append(row)
    return new_list

# Sort list of stations by weekday entry
def sort_list_by_weekday_entry(list_of_data, desc= True):
    return sorted(list_of_data, key=lambda x: x.weekday_entry, reverse= desc)

# Sort list of stations by weekday exit
def sort_list_by_weekday_exit(list_of_data, desc= True):
    return sorted(list_of_data, key=lambda x: x.weekday_exit, reverse= desc)

# Print a table from a list of lists, with correct spacing
def print_table(table_data):
    col_width = max(len(entry) for row in table_data for entry in row) + 2
    for row in table_data:
        print("".join(entry.ljust(col_width) for entry in row))


# print a table from a sorted list of lists
def print_top_list_weekday_entry(sorted_list, number_of_results):
    data_list = []
    data_list.append(sorted_list[0].return_weekday_entry_title())
    for station in sorted_list[0:number_of_results]:
        data_list.append(station.return_weekday_entry_details())
    print_table(data_list)


# print a table from a sorted list of lists
def print_top_list_weekday_exit(sorted_list, number_of_results):
    data_list = []
    data_list.append(sorted_list[0].return_weekday_exit_title())
    for station in sorted_list[0:number_of_results]:
        data_list.append(station.return_weekday_exit_details())
    print_table(data_list)

# print a table from a sorted list of lists
def print_top_list(sorted_entry_list, sorted_exit_list, number_of_results):
    data_list = []
    title_list = sorted_entry_list[0].return_weekday_entry_title()
    title_list.extend(sorted_exit_list[0].return_weekday_exit_title())
    data_list.append(title_list)
    for i in range(0,number_of_results):
        entry = sorted_entry_list[i].return_weekday_entry_details()
        entry.extend(sorted_exit_list[i].return_weekday_exit_details())
        data_list.append(entry)
    print_table(data_list)

# Create a list of the weekday entries
def list_of_weekday_entry(data):
    new_list = []
    for row in data:
        new_list.append(row.weekday_entry)
    return new_list

# Create a list of the weekday exits
def list_of_weekday_exit(data):
    new_list = []
    for row in data:
        new_list.append(row.weekday_exit)
    return new_list

# Create a list of all the boroughs
def unique_list_of_boroughs(data):
    unique_list = set()
    for row in data:
        unique_list.add(row.borough)
    return sorted(list(unique_list))



# Find the average weekday exit from each borough
def average_per_borough(full_list, boroughs):
    list_of_averages= []
    for borough in boroughs:
        total = 0
        number = 0
        for row in full_list:
            if row.borough == borough:
                total += row.weekday_exit
                number +=1
        list_of_averages.append([borough, int(total/number)])
    return list_of_averages

# Print the average weekday exit for each borough
def print_averages(averages_list):
    sorted_list = sorted(averages_list,key= lambda x:x[1], reverse= True)
    data_list = []
    for item in sorted_list:
        new_item = [item[0], str(item[1])]
        data_list.append(new_item)
    data_list.insert(0,["Borough", "Average Weekday Exit"])
    print_table(data_list)

# def print_averages(averages_list):
#     sorted_list = sorted(averages_list,key= lambda x:x[1], reverse= True)
#     rank = 1
#     for item in sorted_list:
#         print(str(rank) + ". Borough: " + item[0] + ",    Average Weekday Exit: " + str(item[1]))
#         rank +=1







# def sort_list_by_weekday_entry(list_of_data, desc= True):
#     return sorted(list_of_data, key=lambda x: x.weekday_entry, reverse= desc)
#
# def sort_list_by_saturday_entry(list_of_data, desc= True):
#     return sorted(list_of_data, key=lambda x: x.saturday_entry, reverse= desc)
#
# def sort_list_by_sunday_entry(list_of_data, desc= True):
#     return sorted(list_of_data, key=lambda x: x.sunday_entry, reverse= desc)
#
# def sort_list_by_saturday_exit(list_of_data, desc= True):
#     return sorted(list_of_data, key=lambda x: x.saturday_exit, reverse= desc)
#
# def sort_list_by_sunday_exit(list_of_data, desc= True):
#     return sorted(list_of_data, key=lambda x: x.sunday_exit, reverse= desc)
#
# def sort_list_by_annual_entry_exit(list_of_data, desc= True):
#     return sorted(list_of_data, key=lambda x: x.annual_entry_exit, reverse= desc)
#
# def print_top_list(sorted_list, number_of_results):
#     print("-----------------------------------------------------------------------------------------------------------------------------------")
#     print(sorted_list[0].return_titles())
#     print("-----------------------------------------------------------------------------------------------------------------------------------")
#     index = 1
#     for station in sorted_list[0:number_of_results]:
#         print(index, ". ")
#         print(station.return_details())
#         index += 1
#
# def print_top_list_annual_entry_exit(sorted_list, number_of_results):
#     print("-----------------------------------------------------------------------------------------------------------------------------------")
#     print(sorted_list[0].return_annual_entry_exit_title())
#     print("-----------------------------------------------------------------------------------------------------------------------------------")
#     index = 1
#     for station in sorted_list[0:number_of_results]:
#         print(index, ". ")
#         print(station.return_annual_entry_exit_details())
#         index += 1
#
#
# def list_of_satureday_entry(data):
#     new_list = []
#     for row in data:
#         new_list.append(row.saturday_entry)
#     return new_list
#
# def list_of_sunday_entry(data):
#     new_list = []
#     for row in data:
#         new_list.append(row.sunday_entry)
#     return new_list
#
# def list_of_saturday_exit(data):
#     new_list = []
#     for row in data:
#         new_list.append(row.saturday_exit)
#     return new_list
#
# def list_of_sunday_exit(data):
#     new_list = []
#     for row in data:
#         new_list.append(row.sunday_exit)
#     return new_list
#
# def list_of_annual_entry_exit(data):
#     new_list = []
#     for row in data:
#         new_list.append(row.annual_entry_exit)
#     return new_list

if __name__ == "__main__":
    under = UndergroundFileReader("C:/Users/RPrince/Documents/python-git-class/london_underground/london_underground/london_underground.xlsx")
    new_list = list_of_station_class(under.data)
    top_weekday_exit = sort_list_by_weekday_exit(new_list)
    print_top_list_weekday_exit(top_weekday_exit, 5)
    x = [1,2,3]

    x.insert(0, [4,5,6])
    print(x)