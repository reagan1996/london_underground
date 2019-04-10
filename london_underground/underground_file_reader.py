from openpyxl import load_workbook

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

    def create_list_of_cell_data(self):
        list_of_data = []
        for row in self.worksheet.values:
            list_of_data.append(list(row))
        return list_of_data[1:]

    def return_cell_value(self, cell_reference):
        return self.worksheet[cell_reference].value

    def print_worksheet(self):
        for item in self.worksheet:
            print(item)
