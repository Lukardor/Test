from dataclasses import dataclass

from forza_horizon6.vehicles.garage import Vehicle
from forza_horizon6.world.open_world import OpenWorld
from forza_horizon6.world.weather import WeatherState


@dataclass
class RaceAIState:
    dynamic_difficulty: float


class RaceAISystem:
    def tick(self, player_vehicle: Vehicle, world: OpenWorld, weather: WeatherState) -> RaceAIState:
        base = 0.5 + min(0.5, player_vehicle.power_hp / 1600)
        climate_penalty = (1.0 - weather.grip_modifier) * 0.35
        map_complexity = min(0.2, len(world.regions) / 100)
        return RaceAIState(dynamic_difficulty=round(base + climate_penalty + map_complexity, 2))
