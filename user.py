class User:
    first_name = " "
    last_name = " "

    def __init__ (self, first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def yoursfirst_name (self):
        print(self.first_name)

    def yourslast_name (self):
        print(self.last_name)

    def yourslastname (self):
        print(self.first_name + " " + self.last_name)
