class Building:
    total = 0

    def __init__(self, number_of_floors, building_type):
        self.number_of_floors = number_of_floors
        self.building_type = building_type
        Building.total += 1

    def __str__(self):
        return f"Building(type={self.building_type}, floors={self.number_of_floors})"

if __name__ == "__main__":
    buildings = []
    for i in range(40):
        building = Building(i + 1, "Residential")
        buildings.append(building)
        print(building)

    print(f"Total buildings created: {Building.total}")
