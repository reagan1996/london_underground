from london_underground.station import Station


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


def sort_list_by_weekday_exit(list_of_data, desc= True):
    return sorted(list_of_data, key=lambda x: x.weekday_exit, reverse= desc)


def print_top_list_weekday_entry(sorted_list, number_of_results):
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print(sorted_list[0].return_weekday_entry_title())
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    index = 1
    for station in sorted_list[0:number_of_results]:
        print(index, ". ")
        print(station.return_weekday_entry_details())
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


def print_top_list(sorted_entry_list, sorted_exit_list, number_of_results):
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print(sorted_entry_list[0].return_weekday_entry_title() + "           " + sorted_exit_list[0].return_weekday_exit_title())
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    index = 1
    for i in range(0,number_of_results):
        print(index, ". ", sorted_entry_list[i].return_weekday_entry_details(), "                 ", sorted_exit_list[i].return_weekday_exit_details())
        index += 1


def list_of_weekday_entry(data):
    new_list = []
    for row in data:
        new_list.append(row.weekday_entry)
    return new_list


def list_of_weekday_exit(data):
    new_list = []
    for row in data:
        new_list.append(row.weekday_exit)
    return new_list


def unique_list_of_boroughs(data):
    unique_list = set()
    for row in data:
        unique_list.add(row.borough)
    return sorted(list(unique_list))


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


def print_averages(averages_list):
    sorted_list = sorted(averages_list,key= lambda x:x[1], reverse= True)
    rank = 1
    for item in sorted_list:
        print(str(rank) + ". Borough: " + item[0] + ",    Average Weekday Exit: " + str(item[1]))
        rank +=1







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