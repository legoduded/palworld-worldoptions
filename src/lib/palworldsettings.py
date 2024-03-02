from enum import Enum
from typing import Dict
import sys
import re


DEATHPENALTY_VALUES = ["None", "Item", "ItemAndEquipment", "All"]


class StructTypes(Enum):
    Int = 1
    Str = 2
    Float = 3
    Bool = 4
    Enum = 5


class ConfigOption:
    def __init__(self, option_name: str, struct: StructTypes, default_value):
        self.option_name = option_name
        self.struct = struct
        self.default_value = default_value

    def _typecast(self, value):
        if self.struct == StructTypes.Int:
            # work around if the values are a float
            return int(float(value))
        elif self.struct == StructTypes.Float:
            return float(value)
        elif self.struct == StructTypes.Bool:
            if value.lower() in ["false", "0"]:
                return False
            else:
                return True
        elif self.struct == StructTypes.Enum:
            if len(value) == 1:
                # Going to assume its an int
                index_value = int(value)
                if index_value >= len(DEATHPENALTY_VALUES):
                    raise AttributeError(f"{value} is not a valid option for DeathPenalty")
                else:
                    return DEATHPENALTY_VALUES[index_value]
            else:
                return value
        else:
            return value

    def is_default(self, value) -> bool:
        return self.default_value == self._typecast(value)

    def json_struct(self, value) -> Dict:
        if self.struct == StructTypes.Enum:

            if len(value) == 1:
                # Going to assume its an int
                index_value = int(value)
                if index_value >= len(DEATHPENALTY_VALUES):
                    raise AttributeError(f"{value} is not a valid option for DeathPenalty")
            else:
                # Lets make this case insensitive
                if value.lower() in [death.lower() for death in DEATHPENALTY_VALUES]:
                    index_value = [death.lower() for death in DEATHPENALTY_VALUES].index(value.lower())
                else:
                    raise AttributeError(f"{value} is not a valid option for DeathPenalty")
            return {
                self.struct.name: {
                    "value": f"EPalOptionWorldDeathPenalty::{DEATHPENALTY_VALUES[index_value]}",
                    "enum_type": "EPalOptionWorldDeathPenalty"
                }
            }
        else:
            return {
                self.struct.name: {
                    "value": self._typecast(value)
                }
            }


class SettingStructs:
    DayTimeSpeedRate = ConfigOption("DayTimeSpeedRate", StructTypes.Float, 1.000000)
    NightTimeSpeedRate = ConfigOption("NightTimeSpeedRate", StructTypes.Float, 1.000000)
    ExpRate = ConfigOption("ExpRate", StructTypes.Float, 1.000000)
    PalCaptureRate = ConfigOption("PalCaptureRate", StructTypes.Float, 1.000000)
    PalSpawnNumRate = ConfigOption("PalSpawnNumRate", StructTypes.Float, 1.000000)
    PalDamageRateAttack = ConfigOption("PalDamageRateAttack", StructTypes.Float, 1.000000)
    PalDamageRateDefense = ConfigOption("PalDamageRateDefense", StructTypes.Float, 1.000000)
    PlayerDamageRateAttack = ConfigOption("PlayerDamageRateAttack", StructTypes.Float, 1.000000)
    PlayerDamageRateDefense = ConfigOption("PlayerDamageRateDefense", StructTypes.Float, 1.000000)
    PlayerStomachDecreaceRate = ConfigOption("PlayerStomachDecreaceRate", StructTypes.Float, 1.000000)
    PlayerStaminaDecreaceRate = ConfigOption("PlayerStaminaDecreaceRate", StructTypes.Float, 1.000000)
    PlayerAutoHPRegeneRate = ConfigOption("PlayerAutoHPRegeneRate", StructTypes.Float, 1.000000)
    PlayerAutoHpRegeneRateInSleep = ConfigOption("PlayerAutoHpRegeneRateInSleep", StructTypes.Float, 1.000000)
    PalStomachDecreaceRate = ConfigOption("PalStomachDecreaceRate", StructTypes.Float, 1.000000)
    PalStaminaDecreaceRate = ConfigOption("PalStaminaDecreaceRate", StructTypes.Float, 1.000000)
    PalAutoHPRegeneRate = ConfigOption("PalAutoHPRegeneRate", StructTypes.Float, 1.000000)
    PalAutoHpRegeneRateInSleep = ConfigOption("PalAutoHpRegeneRateInSleep", StructTypes.Float, 1.000000)
    BuildObjectDamageRate = ConfigOption("BuildObjectDamageRate", StructTypes.Float, 1.000000)
    BuildObjectDeteriorationDamageRate = ConfigOption("BuildObjectDeteriorationDamageRate", StructTypes.Float, 1.000000)
    CollectionDropRate = ConfigOption("CollectionDropRate", StructTypes.Float, 1.000000)
    CollectionObjectHpRate = ConfigOption("CollectionObjectHpRate", StructTypes.Float, 1.000000)
    CollectionObjectRespawnSpeedRate = ConfigOption("CollectionObjectRespawnSpeedRate", StructTypes.Float, 1.000000)
    EnemyDropItemRate = ConfigOption("EnemyDropItemRate", StructTypes.Float, 1.000000)
    DeathPenalty = ConfigOption("DeathPenalty", StructTypes.Enum, "All")
    bEnablePlayerToPlayerDamage = ConfigOption("bEnablePlayerToPlayerDamage", StructTypes.Bool, False)
    bEnableFriendlyFire = ConfigOption("bEnableFriendlyFire", StructTypes.Bool, False)
    bEnableInvaderEnemy = ConfigOption("bEnableInvaderEnemy", StructTypes.Bool, True)
    bActiveUNKO = ConfigOption("bActiveUNKO", StructTypes.Bool, False)
    bEnableAimAssistPad = ConfigOption("bEnableAimAssistPad", StructTypes.Bool, True)
    bEnableAimAssistKeyboard = ConfigOption("bEnableAimAssistKeyboard", StructTypes.Bool, False)
    DropItemMaxNum = ConfigOption("DropItemMaxNum", StructTypes.Int, 3000)
    DropItemMaxNum_UNKO = ConfigOption("DropItemMaxNum_UNKO", StructTypes.Int, 100)
    BaseCampMaxNum = ConfigOption("BaseCampMaxNum", StructTypes.Int, 128)
    BaseCampWorkerMaxNum = ConfigOption("BaseCampWorkerMaxNum", StructTypes.Int, 15)
    DropItemAliveMaxHours = ConfigOption("DropItemAliveMaxHours", StructTypes.Float, 1.000000)
    bAutoResetGuildNoOnlinePlayers = ConfigOption("bAutoResetGuildNoOnlinePlayers", StructTypes.Bool, False)
    AutoResetGuildTimeNoOnlinePlayers = ConfigOption("AutoResetGuildTimeNoOnlinePlayers", StructTypes.Float, 72.000000)
    GuildPlayerMaxNum = ConfigOption("GuildPlayerMaxNum", StructTypes.Int, 20)
    PalEggDefaultHatchingTime = ConfigOption("PalEggDefaultHatchingTime", StructTypes.Float, 72.000000)
    WorkSpeedRate = ConfigOption("WorkSpeedRate", StructTypes.Float, 1.000000)
    bIsMultiplay = ConfigOption("bIsMultiplay", StructTypes.Bool, False)
    bIsPvP = ConfigOption("bIsPvP", StructTypes.Bool, False)
    bCanPickupOtherGuildDeathPenaltyDrop = ConfigOption("bCanPickupOtherGuildDeathPenaltyDrop", StructTypes.Bool, False)
    bEnableNonLoginPenalty = ConfigOption("bEnableNonLoginPenalty", StructTypes.Bool, True)
    bEnableFastTravel = ConfigOption("bEnableFastTravel", StructTypes.Bool, True)
    bIsStartLocationSelectByMap = ConfigOption("bIsStartLocationSelectByMap", StructTypes.Bool, True)
    bExistPlayerAfterLogout = ConfigOption("bExistPlayerAfterLogout", StructTypes.Bool, False)
    bEnableDefenseOtherGuildPlayer = ConfigOption("bEnableDefenseOtherGuildPlayer", StructTypes.Bool, False)
    CoopPlayerMaxNum = ConfigOption("CoopPlayerMaxNum", StructTypes.Int, 4)
    ServerPlayerMaxNum = ConfigOption("ServerPlayerMaxNum", StructTypes.Int, 32)
    ServerName = ConfigOption("ServerName", StructTypes.Str, "Default Palworld Server")
    ServerDescription = ConfigOption("ServerDescription", StructTypes.Str, "")
    AdminPassword = ConfigOption("AdminPassword", StructTypes.Str, "")
    ServerPassword = ConfigOption("ServerPassword", StructTypes.Str, "")
    PublicPort = ConfigOption("PublicPort", StructTypes.Int, 8211)
    PublicIP = ConfigOption("PublicIP", StructTypes.Str, "")
    RCONEnabled = ConfigOption("RCONEnabled", StructTypes.Bool, False)
    RCONPort = ConfigOption("RCONPort", StructTypes.Int, 25575)
    Region = ConfigOption("Region", StructTypes.Str, "")
    bUseAuth = ConfigOption("bUseAuth", StructTypes.Bool, True)
    BanListURL = ConfigOption("BanListURL", StructTypes.Str, "https://api.palworldgame.com/api/banlist.txt")
    bShowPlayerList = ConfigOption("bShowPlayerList", StructTypes.Bool, False)

    @staticmethod
    def get_config_option(option_name: str) -> ConfigOption:
        return getattr(SettingStructs, option_name)


def generate_json_config(config: str) -> Dict:
    json_config = {}
    tokens = re.findall(r'(\w.*?)=([^"].*?|".*?")((?=,)|$)', config)
    for key, value, _ in tokens:
        try:
            if key == "Difficulty":
                continue
            if '"' in value:
                value = re.match(r'^"(.*)"$', value.strip()).group(1)
                # if it was already escaped in the config
                value = value.replace('\\"', '"')
            config_properties = SettingStructs.get_config_option(key)
            if not config_properties.is_default(value):
                json_config[key] = config_properties.json_struct(value)
        except AttributeError:
            print("Error loading", key)
        except ValueError:
            print(f"Error parsing {key}:{value}")
            print("Something looks malformed in your config")
            print("Open a bug report with your config if issues persists")
    return json_config


def parse_config(config: str) -> str:
    return config\
        .replace("OptionSettings=(", "")\
        .strip(") ")


def load_palworldsettings(path: str) -> str:
    with open(path, encoding="utf8") as f:
        config = None
        for line in f:
            if "OptionSettings" in line:
                config = line
        if config is None:
            print("Failed to get OptionSettings")
            print("Is your PalWorldSettings.ini formatted correctly?")
            input("Press RETURN to close")
            sys.exit(1)
    return config


def create_palworldsettings(path: str) -> Dict:
    raw_config = load_palworldsettings(path)
    parsed_config = parse_config(raw_config)
    worldoption["root"]["properties"]["OptionWorldData"]["Struct"]["value"]["Struct"]["Settings"]["Struct"]["value"][
        "Struct"] = generate_json_config(parsed_config)
    return worldoption


worldoption = {
  "header": {
    "magic": 1396790855,
    "save_game_version": 3,
    "package_version": {
      "New": [
        522,
        1008
      ]
    },
    "engine_version_major": 5,
    "engine_version_minor": 1,
    "engine_version_patch": 1,
    "engine_version_build": 0,
    "engine_version": "++UE5+Release-5.1",
    "custom_format_version": 3,
    "custom_format": [
      {
        "id": "40d2fba7-4b48-4ce5-b038-5a75884e499e",
        "value": 7
      },
      {
        "id": "fcf57afa-5076-4283-b9a9-e658ffa02d32",
        "value": 76
      },
      {
        "id": "0925477b-763d-4001-9d91-d6730b75b411",
        "value": 1
      },
      {
        "id": "4288211b-4548-16c6-1a76-67b2507a2a00",
        "value": 1
      },
      {
        "id": "1ab9cecc-0000-6913-0000-4875203d51fb",
        "value": 100
      },
      {
        "id": "4cef9221-470e-d43a-7e60-3d8c16995726",
        "value": 1
      },
      {
        "id": "e2717c7e-52f5-44d3-950c-5340b315035e",
        "value": 7
      },
      {
        "id": "11310aed-2e55-4d61-af67-9aa3c5a1082c",
        "value": 17
      },
      {
        "id": "a7820cfb-20a7-4359-8c54-2c149623cf50",
        "value": 21
      },
      {
        "id": "f6dfbb78-bb50-a0e4-4018-b84d60cbaf23",
        "value": 2
      },
      {
        "id": "24bb7af3-5646-4f83-1f2f-2dc249ad96ff",
        "value": 5
      },
      {
        "id": "76a52329-0923-45b5-98ae-d841cf2f6ad8",
        "value": 5
      },
      {
        "id": "5fbc6907-55c8-40ae-8e67-f1845efff13f",
        "value": 1
      },
      {
        "id": "82e77c4e-3323-43a5-b46b-13c597310df3",
        "value": 0
      },
      {
        "id": "0ffcf66c-1190-4899-b160-9cf84a46475e",
        "value": 1
      },
      {
        "id": "9c54d522-a826-4fbe-9421-074661b482d0",
        "value": 44
      },
      {
        "id": "b0d832e4-1f89-4f0d-accf-7eb736fd4aa2",
        "value": 10
      },
      {
        "id": "e1c64328-a22c-4d53-a36c-8e866417bd8c",
        "value": 0
      },
      {
        "id": "375ec13c-06e4-48fb-b500-84f0262a717e",
        "value": 4
      },
      {
        "id": "e4b068ed-f494-42e9-a231-da0b2e46bb41",
        "value": 40
      },
      {
        "id": "cffc743f-43b0-4480-9391-14df171d2073",
        "value": 37
      },
      {
        "id": "b02b49b5-bb20-44e9-a304-32b752e40360",
        "value": 3
      },
      {
        "id": "a4e4105c-59a1-49b5-a7c5-40c4547edfee",
        "value": 0
      },
      {
        "id": "39c831c9-5ae6-47dc-9a44-9c173e1c8e7c",
        "value": 0
      },
      {
        "id": "78f01b33-ebea-4f98-b9b4-84eaccb95aa2",
        "value": 20
      },
      {
        "id": "6631380f-2d4d-43e0-8009-cf276956a95a",
        "value": 0
      },
      {
        "id": "12f88b9f-8875-4afc-a67c-d90c383abd29",
        "value": 45
      },
      {
        "id": "7b5ae74c-d270-4c10-a958-57980b212a5a",
        "value": 13
      },
      {
        "id": "d7296918-1dd6-4bdd-9de2-64a83cc13884",
        "value": 3
      },
      {
        "id": "c2a15278-bfe7-4afe-6c17-90ff531df755",
        "value": 1
      },
      {
        "id": "6eaca3d4-40ec-4cc1-b786-8bed09428fc5",
        "value": 3
      },
      {
        "id": "29e575dd-e0a3-4627-9d10-d276232cdcea",
        "value": 17
      },
      {
        "id": "af43a65d-7fd3-4947-9873-3e8ed9c1bb05",
        "value": 15
      },
      {
        "id": "6b266cec-1ec7-4b8f-a30b-e4d90942fc07",
        "value": 1
      },
      {
        "id": "0df73d61-a23f-47ea-b727-89e90c41499a",
        "value": 1
      },
      {
        "id": "601d1886-ac64-4f84-aa16-d3de0deac7d6",
        "value": 80
      },
      {
        "id": "5b4c06b7-2463-4af8-805b-bf70cdf5d0dd",
        "value": 10
      },
      {
        "id": "e7086368-6b23-4c58-8439-1b7016265e91",
        "value": 4
      },
      {
        "id": "9dffbcd6-494f-0158-e221-12823c92a888",
        "value": 10
      },
      {
        "id": "f2aed0ac-9afe-416f-8664-aa7ffa26d6fc",
        "value": 1
      },
      {
        "id": "174f1f0b-b4c6-45a5-b13f-2ee8d0fb917d",
        "value": 10
      },
      {
        "id": "35f94a83-e258-406c-a318-09f59610247c",
        "value": 41
      },
      {
        "id": "b68fc16e-8b1b-42e2-b453-215c058844fe",
        "value": 1
      },
      {
        "id": "b2e18506-4273-cfc2-a54e-f4bb758bba07",
        "value": 1
      },
      {
        "id": "64f58936-fd1b-42ba-ba96-7289d5d0fa4e",
        "value": 1
      },
      {
        "id": "697dd581-e64f-41ab-aa4a-51ecbeb7b628",
        "value": 88
      },
      {
        "id": "d89b5e42-24bd-4d46-8412-aca8df641779",
        "value": 41
      },
      {
        "id": "59da5d52-1232-4948-b878-597870b8e98b",
        "value": 8
      },
      {
        "id": "26075a32-730f-4708-88e9-8c32f1599d05",
        "value": 0
      },
      {
        "id": "6f0ed827-a609-4895-9c91-998d90180ea4",
        "value": 2
      },
      {
        "id": "30d58be3-95ea-4282-a6e3-b159d8ebb06a",
        "value": 1
      },
      {
        "id": "717f9ee7-e9b0-493a-88b3-91321b388107",
        "value": 16
      },
      {
        "id": "430c4d19-7154-4970-8769-9b69df90b0e5",
        "value": 15
      },
      {
        "id": "aafe32bd-5395-4c14-b66a-5e251032d1dd",
        "value": 1
      },
      {
        "id": "23afe18e-4ce1-4e58-8d61-c252b953beb7",
        "value": 11
      },
      {
        "id": "a462b7ea-f499-4e3a-99c1-ec1f8224e1b2",
        "value": 4
      },
      {
        "id": "2eb5fdbd-01ac-4d10-8136-f38f3393a5da",
        "value": 5
      },
      {
        "id": "509d354f-f6e6-492f-a749-85b2073c631c",
        "value": 0
      },
      {
        "id": "b6e31b1c-d29f-11ec-857e-9f856f9970e2",
        "value": 1
      },
      {
        "id": "4a56eb40-10f5-11dc-92d3-347eb2c96ae7",
        "value": 2
      },
      {
        "id": "d78a4a00-e858-4697-baa8-19b5487d46b4",
        "value": 18
      },
      {
        "id": "5579f886-933a-4c1f-83ba-087b6361b92f",
        "value": 2
      },
      {
        "id": "612fbe52-da53-400b-910d-4f919fb1857c",
        "value": 1
      },
      {
        "id": "a4237a36-caea-41c9-8fa2-18f858681bf3",
        "value": 5
      },
      {
        "id": "804e3f75-7088-4b49-a4d6-8c063c7eb6dc",
        "value": 5
      },
      {
        "id": "1ed048f4-2f2e-4c68-89d0-53a4f18f102d",
        "value": 1
      },
      {
        "id": "fb680af2-59ef-4ba3-baa8-19b573c8443d",
        "value": 2
      },
      {
        "id": "9950b70e-b41a-4e17-bbcc-fa0d57817fd6",
        "value": 1
      },
      {
        "id": "ab965196-45d8-08fc-b7d7-228d78ad569e",
        "value": 1
      }
    ]
  },
  "root": {
    "save_game_type": "/Script/Pal.PalWorldOptionSaveGame",
    "properties": {
      "Version": {
        "Int": {
          "value": 100
        }
      },
      "OptionWorldData": {
        "Struct": {
          "value": {
            "Struct": {
              "Settings": {
                "Struct": {
                  "value": {
                    "Struct": {
                      "Difficulty": {
                        "Enum": {
                          "value": "EPalOptionWorldDifficulty::Normal",
                          "enum_type": "EPalOptionWorldDifficulty"
                        }
                      }
                    }
                  },
                  "struct_type": {
                    "Struct": "PalOptionWorldSettings"
                  },
                  "struct_id": "00000000-0000-0000-0000-000000000000"
                }
              }
            }
          },
          "struct_type": {
            "Struct": "PalOptionWorldSaveData"
          },
          "struct_id": "00000000-0000-0000-0000-000000000000"
        }
      }
    }
  },
  "extra": [
    0,
    0,
    0,
    0
  ]
}