from dataclasses import dataclass
import random


@dataclass
class Vehicle:
    id: int
    name: str
    class_name: str
    power_hp: int
    weight_kg: int
    tire_grip: float


class GarageFactory:
    CLASSES = [
        "Supersportwagen",
        "Hypercars",
        "Klassiker",
        "Offroad",
        "Driftcars",
        "SUV",
        "Elektroautos",
    ]

    def generate_vehicle_pool(self, total: int = 700) -> list[Vehicle]:
        cars: list[Vehicle] = []
        for i in range(total):
            class_name = self.CLASSES[i % len(self.CLASSES)]
            cars.append(
                Vehicle(
                    id=i,
                    name=f"FH6 Concept {i:03d}",
                    class_name=class_name,
                    power_hp=250 + (i % 650),
                    weight_kg=900 + (i % 1200),
                    tire_grip=0.82 + ((i % 18) * 0.01),
                )
            )
        return cars

    def spawn_player_starter_car(self) -> Vehicle:
        base = self.generate_vehicle_pool(20)
        return random.choice(base)
