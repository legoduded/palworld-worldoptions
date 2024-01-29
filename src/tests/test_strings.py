from lib.palworldsettings import load_palworldsettings, parse_config, generate_json_config
from typing import Dict
import unittest


def load_data(path: str) -> Dict:
    raw_config = load_palworldsettings(path)
    parsed_config = parse_config(raw_config)
    return generate_json_config(parsed_config)


STRING_VALUES = {'ServerName': {'Str': {'value': 'MY Palworld Server'}}, 'ServerDescription': {'Str': {'value': 'This is my server'}}, 'AdminPassword': {'Str': {'value': 's3cure'}}, 'ServerPassword': {'Str': {'value': 'passw0rd'}}, 'PublicIP': {'Str': {'value': '127.0.0.1'}}, 'Region': {'Str': {'value': 'Tokyo'}}, 'BanListURL': {'Str': {'value': 'https://api.palworldgame.com/api/banlist_test.txt'}}}
STRING_VALUES_COMMA = {'ServerName': {'Str': {'value': '[MY] Palworld Server'}}, 'ServerDescription': {'Str': {'value': 'This is my server'}}, 'ServerPassword': {'Str': {'value': 'i,have,commas,'}}}
STRING_VALUES_QUOTES = {'ServerName': {'Str': {'value': '"MY" Palworld Server'}}, 'ServerDescription': {'Str': {'value': 'This is "my" server'}}}


class TestStrings(unittest.TestCase):
    def test_strings(self):
        data = load_data("tests/configs/Strings.ini")
        assert(STRING_VALUES == data)

    def test_strings_comma(self):
        data = load_data("tests/configs/StringsComma.ini")
        assert(STRING_VALUES_COMMA == data)

    def test_strings_quotes(self):
        data = load_data("tests/configs/StringsQuotes.ini")
        assert(STRING_VALUES_QUOTES == data)
