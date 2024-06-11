class Building:
    def __init__(self, number_of_floors, building_type):
        self.number_of_floors = number_of_floors
        self.building_type = building_type

    def __eq__(self, other):
        if isinstance(other, Building):
            return self.number_of_floors == other.number_of_floors and self.building_type == other.building_type
        return False

if __name__ == "__main__":
    building1 = Building(5, "Residential")
    building2 = Building(5, "Residential")
    building3 = Building(10, "Commercial")

    print(building1 == building2)
    print(building1 == building3)
