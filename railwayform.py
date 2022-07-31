class RailwayForm:
    FormType = "Reservation Form"

    def printdata(self):
        print(f"My name is {self.name}")
        print(f"Train name is {self.train}")


ticketapplication = RailwayForm()
ticketapplication.name = "Hamid"
ticketapplication.train = "Orange Train"
ticketapplication.printdata()