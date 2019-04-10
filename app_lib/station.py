class Station:
    def __init__(self, name, borough, weekday_entry, saturday_entry, sunday_entry, weekday_exit, saturday_exit, sunday_exit, annual_entry_exit):
        self.station_name = name
        self.borough = borough
        self.weekday_entry = weekday_entry
        self.saturday_entry = saturday_entry
        self.sunday_entry = sunday_entry
        self.weekday_exit = weekday_exit
        self.saturday_exit = saturday_exit
        self.sunday_exit = sunday_exit
        self.annual_entry_exit = annual_entry_exit

    def return_titles(self):
        return "Station Name, Borough, Weekday- Entry, Saturday- Entry, Sunday- Entry, Weekday- Exit, Sturday- Exit, Sunday- Exit, " + \
               "Annual- Entry + Exit"

    def return_weekday_exit_title(self):
        return "Station Name, Borough, Weekday- Exit"

    def return_annual_entry_exit_title(self):
        return "Station Name, Borough, Annual- Entry + Exit"

    def return_details(self):
        return self.station_name + ", " + self.borough + ", " + str(self.weekday_entry) + \
        ", " + str(self.saturday_exit) + ", " + str(self.sunday_exit) + ", " + \
        str(self.weekday_exit) + ", " + str(self.saturday_exit) + ", " + str(self.sunday_exit) +\
        ", " + str(self.annual_entry_exit)

    def return_weekday_exit_details(self):
        return self.station_name + ", " + self.borough + ", " + str(self.weekday_exit)

    def return_annual_entry_exit_details(self):
        return self.station_name + ", " + self.borough + ", " + str(self.annual_entry_exit)