from dataclasses import dataclass

from forza_horizon6.vehicles.garage import Vehicle


@dataclass
class PhysicsState:
    speed_kmh: float
    traction: float
    damage_ratio: float


class VehicleDynamics:
    def step(self, vehicle: Vehicle, delta_time: float) -> PhysicsState:
        accel = max(2.0, vehicle.power_hp / max(vehicle.weight_kg, 1) * 14.0)
        speed = min(420.0, accel * delta_time * 360)
        traction = min(1.0, vehicle.tire_grip)
        damage_ratio = 0.0
        return PhysicsState(speed_kmh=speed, traction=traction, damage_ratio=damage_ratio)
