from lib.palworldsettings import load_palworldsettings, parse_config, generate_json_config
from typing import Dict
import unittest


def load_data(path: str) -> Dict:
    raw_config = load_palworldsettings(path)
    parsed_config = parse_config(raw_config)
    return generate_json_config(parsed_config)


FloatValues = {'DayTimeSpeedRate': {'Float': {'value': 1.1}}, 'NightTimeSpeedRate': {'Float': {'value': 1.1}}, 'ExpRate': {'Float': {'value': 1.1}}, 'PalCaptureRate': {'Float': {'value': 1.1}}, 'PalSpawnNumRate': {'Float': {'value': 1.1}}, 'PalDamageRateAttack': {'Float': {'value': 1.1}}, 'PalDamageRateDefense': {'Float': {'value': 1.1}}, 'PlayerDamageRateAttack': {'Float': {'value': 1.1}}, 'PlayerDamageRateDefense': {'Float': {'value': 1.1}}, 'PlayerStomachDecreaceRate': {'Float': {'value': 1.1}}, 'PlayerStaminaDecreaceRate': {'Float': {'value': 1.1}}, 'PlayerAutoHPRegeneRate': {'Float': {'value': 1.1}}, 'PlayerAutoHpRegeneRateInSleep': {'Float': {'value': 1.1}}, 'PalStomachDecreaceRate': {'Float': {'value': 1.1}}, 'PalStaminaDecreaceRate': {'Float': {'value': 1.1}}, 'PalAutoHPRegeneRate': {'Float': {'value': 1.1}}, 'PalAutoHpRegeneRateInSleep': {'Float': {'value': 1.1}}, 'BuildObjectDamageRate': {'Float': {'value': 1.1}}, 'BuildObjectDeteriorationDamageRate': {'Float': {'value': 1.1}}, 'CollectionDropRate': {'Float': {'value': 1.1}}, 'CollectionObjectHpRate': {'Float': {'value': 1.1}}, 'CollectionObjectRespawnSpeedRate': {'Float': {'value': 1.1}}, 'EnemyDropItemRate': {'Float': {'value': 1.1}}, 'DropItemAliveMaxHours': {'Float': {'value': 1.1}}, 'AutoResetGuildTimeNoOnlinePlayers': {'Float': {'value': 72.1}}, 'PalEggDefaultHatchingTime': {'Float': {'value': 72.1}}, 'WorkSpeedRate': {'Float': {'value': 1.1}}}
FloatIntValues = {'DayTimeSpeedRate': {'Float': {'value': 2.0}}, 'NightTimeSpeedRate': {'Float': {'value': 2.0}}, 'ExpRate': {'Float': {'value': 2.0}}, 'PalCaptureRate': {'Float': {'value': 2.0}}, 'PalSpawnNumRate': {'Float': {'value': 2.0}}, 'PalDamageRateAttack': {'Float': {'value': 2.0}}, 'PalDamageRateDefense': {'Float': {'value': 2.0}}, 'PlayerDamageRateAttack': {'Float': {'value': 2.0}}, 'PlayerDamageRateDefense': {'Float': {'value': 2.0}}, 'PlayerStomachDecreaceRate': {'Float': {'value': 2.0}}, 'PlayerStaminaDecreaceRate': {'Float': {'value': 2.0}}, 'PlayerAutoHPRegeneRate': {'Float': {'value': 2.0}}, 'PlayerAutoHpRegeneRateInSleep': {'Float': {'value': 2.0}}, 'PalStomachDecreaceRate': {'Float': {'value': 2.0}}, 'PalStaminaDecreaceRate': {'Float': {'value': 2.0}}, 'PalAutoHPRegeneRate': {'Float': {'value': 2.0}}, 'PalAutoHpRegeneRateInSleep': {'Float': {'value': 2.0}}, 'BuildObjectDamageRate': {'Float': {'value': 2.0}}, 'BuildObjectDeteriorationDamageRate': {'Float': {'value': 2.0}}, 'CollectionDropRate': {'Float': {'value': 2.0}}, 'CollectionObjectHpRate': {'Float': {'value': 2.0}}, 'CollectionObjectRespawnSpeedRate': {'Float': {'value': 2.0}}, 'EnemyDropItemRate': {'Float': {'value': 2.0}}, 'DropItemAliveMaxHours': {'Float': {'value': 2.0}}, 'AutoResetGuildTimeNoOnlinePlayers': {'Float': {'value': 24.0}}, 'PalEggDefaultHatchingTime': {'Float': {'value': 24.0}}, 'WorkSpeedRate': {'Float': {'value': 2.0}}}


class TestFloats(unittest.TestCase):
    def test_floats(self):
        data = load_data("tests/configs/Floats.ini")
        assert(FloatValues == data)

    def test_floats_int(self):
        data = load_data("tests/configs/FloatsInt.ini")
        assert(FloatIntValues == data)
