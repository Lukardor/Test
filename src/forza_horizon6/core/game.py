from dataclasses import dataclass

from forza_horizon6.world.open_world import OpenWorld
from forza_horizon6.world.weather import WeatherSystem
from forza_horizon6.vehicles.garage import GarageFactory
from forza_horizon6.physics.vehicle_dynamics import VehicleDynamics
from forza_horizon6.ai.traffic_ai import TrafficAISystem
from forza_horizon6.ai.race_ai import RaceAISystem
from forza_horizon6.multiplayer.server import MultiplayerServer
from forza_horizon6.ui.menu import MainMenu
from forza_horizon6.gameplay.story import StoryCampaign


@dataclass
class Game:
    world: OpenWorld | None = None
    weather: WeatherSystem | None = None
    garage_factory: GarageFactory | None = None
    dynamics: VehicleDynamics | None = None
    traffic_ai: TrafficAISystem | None = None
    race_ai: RaceAISystem | None = None
    multiplayer: MultiplayerServer | None = None
    menu: MainMenu | None = None
    story: StoryCampaign | None = None

    def bootstrap(self) -> None:
        self.world = OpenWorld.build_default_map()
        self.weather = WeatherSystem()
        self.garage_factory = GarageFactory()
        self.dynamics = VehicleDynamics()
        self.traffic_ai = TrafficAISystem(max_npc=250)
        self.race_ai = RaceAISystem()
        self.multiplayer = MultiplayerServer(max_players=100)
        self.menu = MainMenu()
        self.story = StoryCampaign()

    def run_demo_loop(self, ticks: int = 60) -> None:
        assert self.world and self.weather and self.garage_factory and self.dynamics
        assert self.traffic_ai and self.race_ai and self.multiplayer and self.menu and self.story

        self.menu.render()
        print(self.story.start_intro())

        player_car = self.garage_factory.spawn_player_starter_car()
        print(f"Starter car: {player_car.name} ({player_car.class_name})")

        for i in range(ticks):
            current_weather = self.weather.tick(i)
            npc_state = self.traffic_ai.tick(self.world, current_weather)
            race_state = self.race_ai.tick(player_car, self.world, current_weather)
            physics_state = self.dynamics.step(player_car, delta_time=1 / 60)

            print(
                f"Tick {i:02d}: weather={current_weather.name}, "
                f"npc={npc_state.active_npc}, ai_difficulty={race_state.dynamic_difficulty:.2f}, "
                f"speed={physics_state.speed_kmh:.1f} km/h"
            )
