from class_methods_demo_class import Vehicle

boat = Vehicle.water_vehicle("Minnow", (30, 40, 10))
print(boat.name)
print(boat.num_wheels)
print(boat.volume())

print()
car = Vehicle.road_vehicle("Kitt", (4, 3, 1.5), 4)
print(car.name)
print(car.num_wheels)
print(car.volume())

print()
print(f"{Vehicle.all_float(boat)}")
print(f"{Vehicle.all_float(boat, boat)}")
print(f"{Vehicle.all_float(boat, boat, car)}")
