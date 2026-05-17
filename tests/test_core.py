from forza_horizon6.world.open_world import OpenWorld
from forza_horizon6.vehicles.garage import GarageFactory


def test_world_has_required_regions():
    world = OpenWorld.build_default_map()
    biomes = {r.biome for r in world.regions}
    for required in ["Großstadt", "Wüste", "Wald", "Berge", "Küstenstraßen", "Rennstrecken"]:
        assert required in biomes


def test_vehicle_pool_size():
    garage = GarageFactory()
    pool = garage.generate_vehicle_pool(700)
    assert len(pool) == 700
