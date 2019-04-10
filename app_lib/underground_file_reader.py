from openpyxl import load_workbook
from station import Station


class UndergroundFileReader:

    def __init__(self, file_name_and_path):
        self.import_file(file_name_and_path)
        self.worksheet = self.workbook.active
        self.data = self.create_list_of_cell_data()

    def import_file(self, file_name):
        try:
            self.workbook = load_workbook(file_name, read_only=True)
        except FileNotFoundError:
            raise FileNotFoundError("no file found")



    def return_cell_value(self, cell_reference):
        return self.worksheet[cell_reference].value

    def print_worksheet(self):
        for item in self.worksheet:
            print(item)

    def create_list_of_cell_data(self):
        list_of_data = []
        for row in self.worksheet.values:
            list_of_data.append(list(row))
        return list_of_data[1:]




if __name__ == "__main__":
    under = UndergroundFileReader("london_underground.xlsx")

    def list_of_station_class(data):
        list_of_stations = []
        for row in data:
            list_of_stations.append(Station(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        return list_of_stations

    new_list = list_of_station_class(under.data)
    print(new_list[0].station_name)

    def selected_borough(list_of_data, borough):
        new_list = []
        for row in list_of_data:
            if row.borough == borough:
                new_list.append(row)
        return new_list

    def sort_list_by_weekday_entry(list_of_data):
        return sorted(list_of_data, key=lambda x: x.weekday_entry)

    def sort_list_by_saturday_entry(list_of_data):
        return sorted(list_of_data, key=lambda x: x.saturday_entry)

    def sort_list_by_sunday_entry(list_of_data):
        return sorted(list_of_data, key=lambda x: x.sunday_entry)

    def sort_list_by_weekday_exit(list_of_data):
        return sorted(list_of_data, key=lambda x: x.weekday_exit)

    def sort_list_by_saturday_exit(list_of_data):
        return sorted(list_of_data, key=lambda x: x.saturday_exit)

    def sort_list_by_sunday_exit(list_of_data):
        return sorted(list_of_data, key=lambda x: x.sunday_exit)

    def sort_list_by_annual_entry_exit(list_of_data):
        return sorted(list_of_data, key=lambda x: x.annual_entry_exit)

    sorted_list = sort_list_by_weekday_entry(new_list)





    print("-----------------------------------------------------------------------------------------------------------------------------------")
    sorted_list[0].print_titles()
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    index = 1
    for station in sorted_list[0:10]:
        print(index, ". ")
        station.print_details()
        index += 1

