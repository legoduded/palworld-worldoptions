from lib.palworldsettings import load_palworldsettings, parse_config, generate_json_config
from typing import Dict
import unittest


def load_data(path: str) -> Dict:
    raw_config = load_palworldsettings(path)
    parsed_config = parse_config(raw_config)
    return generate_json_config(parsed_config)


INT_VALUES = {'DropItemMaxNum': {'Int': {'value': 2000}}, 'DropItemMaxNum_UNKO': {'Int': {'value': 50}}, 'BaseCampMaxNum': {'Int': {'value': 64}}, 'BaseCampWorkerMaxNum': {'Int':{'value': 20}}, 'GuildPlayerMaxNum': {'Int': {'value': 40}}, 'CoopPlayerMaxNum': {'Int': {'value': 8}}, 'ServerPlayerMaxNum': {'Int': {'value': 20}}, 'PublicPort': {'Int': {'value': 9000}}, 'RCONPort': {'Int': {'value': 25576}}}


class TestInts(unittest.TestCase):
    def test_ints(self):
        data = load_data("tests/configs/Ints.ini")
        assert(INT_VALUES == data)

    def test_ints_floats(self):
        data = load_data("tests/configs/IntsFloats.ini")
        assert(INT_VALUES == data)
