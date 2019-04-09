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
        list = []
        for row in self.worksheet.values:
            new_station = Station(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            list.append(new_station)

        return list[1:]


if __name__ == "__main__":
    under = UndergroundFileReader("london_underground.xlsx")
    print(under.data[0].station_name)
    x = UndergroundFileReader("no_file.xlsx")