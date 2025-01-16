class Flight:
    def __init__(self, flight_number, origin, destination, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, passenger_name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger_name)
            print(f"Passenger {passenger_name} added to flight {self.flight_number}.")
        else:
            print("Flight is full. Cannot add passenger.")

    def remove_passenger(self, passenger_name):
        if passenger_name in self.passengers:
            self.passengers.remove(passenger_name)
            print(f"Passenger {passenger_name} removed from flight {self.flight_number}.")
        else:
            print(f"Passenger {passenger_name} not found on flight {self.flight_number}.")

    def view_passengers(self):
        if not self.passengers:
            print("No passengers on this flight.")
        else:
            print(f"Passengers on flight {self.flight_number}: {', '.join(self.passengers)}")

class AviationManagementSystem:
    def __init__(self):
        self.flights = {}

    def add_flight(self, flight_number, origin, destination, capacity):
        if flight_number not in self.flights:
            self.flights[flight_number] = Flight(flight_number, origin, destination, capacity)
            print(f"Flight {flight_number} added.")
        else:
            print(f"Flight {flight_number} already exists.")

    def view_flights(self):
        if not self.flights:
            print("No flights available.")
        else:
            print("Available Flights:")
            for flight in self.flights.values():
                print(f"Flight Number: {flight.flight_number}, Origin: {flight.origin}, Destination: {flight.destination}, Capacity: {flight.capacity}")

def main():
    aviation_system = AviationManagementSystem()

    while True:
        print("\nAviation Management System")
        print("1. Add Flight")
        print("2. View Flights")
        print("3. Add Passenger to Flight")
        print("4. Remove Passenger from Flight")
        print("5. View Passengers on Flight")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            flight_number = input("Enter flight number: ")
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            capacity = int(input("Enter capacity: "))
            aviation_system.add_flight(flight_number, origin, destination, capacity)

        elif choice == '2':
            aviation_system.view_flights()

        elif choice == '3':
            flight_number = input("Enter flight number: ")
            passenger_name = input("Enter passenger name: ")
            if flight_number in aviation_system.flights:
                aviation_system.flights[flight_number].add_passenger(passenger_name)
            else:
                print(f"Flight {flight_number} not found.")

        elif choice == '4':
            flight_number = input("Enter flight number: ")
            passenger_name = input("Enter passenger name: ")
            if flight_number in aviation_system.flights:
                aviation_system.flights[flight_number].remove_passenger(passenger_name)
            else:
                print(f"Flight {flight_number} not found.")

        elif choice == '5':
            flight_number = input("Enter flight number: ")
            if flight_number in aviation_system.flights:
                aviation_system.flights[flight_number].view_passengers()
            else:
                print(f"Flight {flight_number} not found.")

        elif choice == '6':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
