from typing import Protocol


class Vehicle(Protocol):
    def drive(self) -> None:
        ...


class SmallVehicle(Protocol):
    def park_in_compact_spot(self) -> None:
        ...


class Car:
    def drive(self) -> None:
        print("drive a car on the road")

    def park_in_compact_spot(self) -> None:
        ...


class Motorcycle:
    def park_in_compact_spot(self) -> None:
        ...


class Boat:
    def drive(self) -> None:
        print("drive a boat on the water")


class Plane:
    def fly(self) -> None:
        print("fly a plane in the air")


def drive_it(vehicle: Vehicle) -> None:
    vehicle.drive()


def park_in_compact_spot(vehicle: SmallVehicle) -> None:
    vehicle.park_in_compact_spot()


car = Car()
boat = Boat()
plane = Plane()
motorcycle = Motorcycle()

drive_it(car)
drive_it(boat)
# drive_it(plane)

park_in_compact_spot(car)
park_in_compact_spot(motorcycle)
# park_in_compact_spot(plane)
