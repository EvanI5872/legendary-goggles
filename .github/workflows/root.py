python
class Aircraft:
    def __init__(self, name, speed, altitude):
        self.name = name
        self.speed = speed
        self.altitude = altitude

    def take_off(self):
        print(f"{self.name} is taking off.")

    def fly(self):
        print(f"{self.name} is flying at {self.speed} knots and {self.altitude} feet.")

    def land(self):
        print(f"{self.name} is landing.")


class FlightSimulator:
    def __init__(self):
        self.aircrafts = []

    def add_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)

    def simulate_flight(self):
        for aircraft in self.aircrafts:
            aircraft.take_off()
            aircraft.fly()
            aircraft.land()


# Creating aircraft instances
aircraft1 = Aircraft("Boeing 747", 500, 30000)
aircraft2 = Aircraft("Airbus A320", 400, 25000)
aircraft3 = Aircraft("Cessna 172", 100, 10000)

# Creating flight simulator instance
simulator = FlightSimulator()

# Adding aircraft to the simulator
simulator.add_aircraft(aircraft1)
simulator.add_aircraft(aircraft2)
simulator.add_aircraft(aircraft3)

# Simulating flight for all aircraft
simulator.simulate_flight()
class Runway:
    def __init__(self, name, location, length, width, orientation):
        self.name = name
        self.location = location
        self.length = length
        self.width = width
        self.orientation = orientation

    def get_details(self):
        return f"Runway: {self.name}\nLocation: {self.location}\nLength: {self.length} meters\nWidth: {self.width} meters\nOrientation: {self.orientation} degrees"


# Creating runway instances
runway1 = Runway("Runway 09/27", "JFK International Airport, New York, USA", 3658, 45, 90)
runway2 = Runway("Runway 18/36", "Cape Town International Airport, Cape Town, South Africa", 3300, 60, 180)

# Accessing runway details
print(runway1.get_details())
print(runway2.get_details())
