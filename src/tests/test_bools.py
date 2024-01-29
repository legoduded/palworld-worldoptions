from lib.palworldsettings import load_palworldsettings, parse_config, generate_json_config
from typing import Dict
import unittest


def load_data(path: str) -> Dict:
    raw_config = load_palworldsettings(path)
    parsed_config = parse_config(raw_config)
    return generate_json_config(parsed_config)


BoolsFalse = {'bEnableInvaderEnemy': {'Bool': {'value': False}}, 'bEnableAimAssistPad': {'Bool': {'value': False}}, 'bEnableNonLoginPenalty': {'Bool': {'value': False}}, 'bEnableFastTravel': {'Bool': {'value': False}}, 'bIsStartLocationSelectByMap': {'Bool': {'value': False}}, 'bUseAuth': {'Bool': {'value': False}}}
BoolsTrue = {'bEnablePlayerToPlayerDamage': {'Bool': {'value': True}}, 'bEnableFriendlyFire': {'Bool': {'value': True}}, 'bActiveUNKO': {'Bool': {'value': True}}, 'bEnableAimAssistKeyboard': {'Bool': {'value': True}}, 'bAutoResetGuildNoOnlinePlayers': {'Bool': {'value': True}}, 'bIsMultiplay': {'Bool': {'value': True}}, 'bIsPvP': {'Bool':{'value': True}}, 'bCanPickupOtherGuildDeathPenaltyDrop': {'Bool': {'value': True}}, 'bExistPlayerAfterLogout': {'Bool': {'value': True}}, 'bEnableDefenseOtherGuildPlayer': {'Bool': {'value': True}}, 'RCONEnabled': {'Bool': {'value': True}}}


class TestBools(unittest.TestCase):
    def test_bools_false_upper(self):
        data = load_data("tests/configs/BoolsFalseUpper.ini")
        assert(BoolsFalse == data)

    def test_bools_false_lower(self):
        data = load_data("tests/configs/BoolsFalseLower.ini")
        assert(BoolsFalse == data)

    def test_bools_false_int(self):
        data = load_data("tests/configs/BoolsFalseInt.ini")
        assert(BoolsFalse == data)

    def test_bools_true_upper(self):
        data = load_data("tests/configs/BoolsTrueUpper.ini")
        assert(BoolsTrue == data)

    def test_bools_true_lower(self):
        data = load_data("tests/configs/BoolsTrueLower.ini")
        assert(BoolsTrue == data)

    def test_bools_true_int(self):
        data = load_data("tests/configs/BoolsTrueInt.ini")
        assert(BoolsTrue == data)
