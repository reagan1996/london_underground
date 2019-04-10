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

    def print_titles(self):
        print("Station Name, Borough, Weekday- Entry, Saturday- Entry, Sunday- Entry, Weekday- Exit, Sturday- Exit, Sunday- Exit, " +
              "Annual- Entry + Exit")

    def print_details(self):
        print(self.station_name, ", ", self.borough, ", ", self.weekday_entry,
              ", ", self.saturday_exit, ", ", self.sunday_exit, ", ",
              self.weekday_exit, ", ", self.saturday_exit, ", ", self.sunday_exit,
              ", ", self.annual_entry_exit)