from dataclasses import dataclass

from forza_horizon6.world.open_world import OpenWorld
from forza_horizon6.world.weather import WeatherState


@dataclass
class TrafficState:
    active_npc: int


class TrafficAISystem:
    def __init__(self, max_npc: int) -> None:
        self.max_npc = max_npc

    def tick(self, world: OpenWorld, weather: WeatherState) -> TrafficState:
        weather_factor = weather.visibility
        density = int(self.max_npc * weather_factor)
        world_bonus = int(world.total_size_km2 / 50)
        return TrafficState(active_npc=max(10, density - world_bonus))
