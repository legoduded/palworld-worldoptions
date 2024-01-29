from lib.palworldsettings import create_palworldsettings
from main import save_worldoptions
from lib.palsav import convert_to_json
import unittest
import os

UESAVE_PATH = "uesave/uesave.exe"
WORLDSAVE = "WorldOption.sav"

class TestConverting(unittest.TestCase):
    def test_all_configs(self):
        config_path = "tests/configs/"
        for file in os.listdir(config_path):
            config_filepath = os.path.join(config_path, file)
            if os.path.isfile(config_filepath) and 'ini' in file:
                try:
                    before_convert = create_palworldsettings(config_filepath)
                    save_worldoptions(UESAVE_PATH, before_convert, "")
                    after_convert = convert_to_json(UESAVE_PATH, WORLDSAVE)
                    assert(before_convert == after_convert)
                except Exception:
                    assert False
                finally:
                    if os.path.exists(WORLDSAVE):
                        os.remove(WORLDSAVE)
