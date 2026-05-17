from dataclasses import dataclass


@dataclass
class Region:
    name: str
    biome: str
    size_km2: float


@dataclass
class OpenWorld:
    name: str
    total_size_km2: float
    regions: list[Region]
    hidden_locations: int

    @staticmethod
    def build_default_map() -> "OpenWorld":
        regions = [
            Region("Neo Vista", "Großstadt", 120.0),
            Region("Sol Dunes", "Wüste", 250.0),
            Region("Pine Crown", "Wald", 180.0),
            Region("Sierra Aurora", "Berge", 210.0),
            Region("Costa Azul", "Küstenstraßen", 150.0),
            Region("Riverton", "Dörfer", 90.0),
            Region("Interstate Grid", "Autobahnen", 160.0),
            Region("Apex Park", "Rennstrecken", 40.0),
        ]
        return OpenWorld(
            name="Forza Horizon 6 - Continental Festival Map",
            total_size_km2=sum(r.size_km2 for r in regions),
            regions=regions,
            hidden_locations=320,
        )
