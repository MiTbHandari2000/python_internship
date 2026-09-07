print("\n--- Create Flight class with seat booking functionality ---")

class Flight:
    def __init__(self):
        
        self.seats={}
        for seat_number in range(1,31):
            self.seats[seat_number] = "available"

    def book_seat(self,seat_number):

        if seat_number in self.seats:
            if self.seats[seat_number] == "available":
                self.seats[seat_number] = "booked"
                print("the seat has been successfully booked")
                return True
            else:
                print("Seat is already booked")
                return False
        else:
            print("Enter the valid Seat number ")
            return False
        
        
booking1 = Flight()
print(booking1.book_seat(10))


