from openpyxl import load_workbook
from station import Station


class UndergroundFileReader:

    def __init__(self, file_name_and_path):
        self.workbook = self.import_excel_workbook(file_name_and_path)
        self.worksheet = self.workbook.active
        self.data = self.create_list_of_cell_data()

    def import_excel_workbook(self, file_name):
        workbook = ""
        try:
            workbook = load_workbook(file_name, read_only=True)

        except FileNotFoundError as error_message:
            print(error_message)
            raise

        finally:
            return workbook

    def return_cell_value(self, cell_reference):
        return self.worksheet[cell_reference].value

    def print_worksheet(self):
        for item in self.worksheet:
            print(item)

    def create_list_of_cell_data(self):
        list = []
        for row in self.worksheet.values:
            new_station = Station(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            list.append(new_station)

        return list[1:]
