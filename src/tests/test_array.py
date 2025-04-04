from lib.palworldsettings import load_palworldsettings, parse_config, generate_json_config
from typing import Dict
import unittest


def load_data(path: str) -> Dict:
    raw_config = load_palworldsettings(path)
    parsed_config = parse_config(raw_config)
    return generate_json_config(parsed_config)


X_PLAY_PLAT_STEAM = {"CrossplayPlatforms": {"Array": {"array_type": "EnumProperty", "value": {"Base": {"Enum": ["EPalAllowConnectPlatform::Steam"]}}}}}
X_PLAY_PLAT_STEAM_MAC = {"CrossplayPlatforms": {"Array": {"array_type": "EnumProperty", "value": {"Base": {"Enum": ["EPalAllowConnectPlatform::Steam", "EPalAllowConnectPlatform::Mac"]}}}}}
X_PLAY_PLAT_ALL = {}
X_PLAY_PLAT_NONE = {"CrossplayPlatforms": {"Array": {"array_type": "EnumProperty", "value": {"Base": {"Enum": []}}}}}


class TestCrossplayPlatformsSingle(unittest.TestCase):
    def test_value_steam(self):
        data = load_data("tests/configs/CrossplayPlatforms1.ini")
        print(data)
        assert(X_PLAY_PLAT_STEAM == data)

    def test_value_steam_mac(self):
        data = load_data("tests/configs/CrossplayPlatforms2.ini")
        print(data)
        assert(X_PLAY_PLAT_STEAM_MAC == data)

    def test_value_none(self):
        data = load_data("tests/configs/CrossplayPlatforms3.ini")
        print(data)
        assert(X_PLAY_PLAT_NONE == data)

    def test_value_all(self):
        data = load_data("tests/configs/CrossplayPlatforms4.ini")
        print(data)
        assert(X_PLAY_PLAT_ALL == data)




