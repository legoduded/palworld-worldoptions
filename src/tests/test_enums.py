from lib.palworldsettings import load_palworldsettings, parse_config, generate_json_config
from typing import Dict
import unittest


def load_data(path: str) -> Dict:
    raw_config = load_palworldsettings(path)
    parsed_config = parse_config(raw_config)
    return generate_json_config(parsed_config)


DP_NONE = {'DeathPenalty': {'Enum': {'value': 'EPalOptionWorldDeathPenalty::None', 'enum_type': 'EPalOptionWorldDeathPenalty'}}}
DP_ITEM = {'DeathPenalty': {'Enum': {'value': 'EPalOptionWorldDeathPenalty::Item', 'enum_type': 'EPalOptionWorldDeathPenalty'}}}
DP_IAE = {'DeathPenalty': {'Enum': {'value': 'EPalOptionWorldDeathPenalty::ItemAndEquipment', 'enum_type': 'EPalOptionWorldDeathPenalty'}}}
DP_EMPTY = {}


class TestDeathPenaltyNames(unittest.TestCase):
    def test_value_None(self):
        data = load_data("tests/configs/DeathPenaltyNone.ini")
        assert(DP_NONE == data)

    def test_value_Item(self):
        data = load_data("tests/configs/DeathPenaltyItem.ini")
        assert(DP_ITEM == data)

    def test_value_IAE(self):
        data = load_data("tests/configs/DeathPenaltyItemAndEquipment.ini")
        assert(DP_IAE == data)

    def test_value_All(self):
        data = load_data("tests/configs/DeathPenaltyAll.ini")
        assert(DP_EMPTY == data)

    def test_value_Perma(self):
        data = load_data("tests/configs/DeathPenaltyPerma.ini")
        assert(DP_EMPTY == data)


class TestDeathPenaltyInts(unittest.TestCase):
    def test_value_0(self):
        data = load_data("tests/configs/DeathPenalty0.ini")
        assert(DP_NONE == data)

    def test_value_1(self):
        data = load_data("tests/configs/DeathPenalty1.ini")
        assert(DP_ITEM == data)

    def test_value_2(self):
        data = load_data("tests/configs/DeathPenalty2.ini")
        assert(DP_IAE == data)

    def test_value_3(self):
        data = load_data("tests/configs/DeathPenalty3.ini")
        assert(DP_EMPTY == data)

    def test_value_4(self):
        data = load_data("tests/configs/DeathPenalty4.ini")
        assert(DP_EMPTY == data)




