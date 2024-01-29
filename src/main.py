#!/usr/bin/env python3

from typing import Dict
import argparse
import sys
import os
from lib.palsav import convert_to_save
from lib.palworldsettings import create_palworldsettings


def exceptionhook(type, value, traceback, oldhook=sys.excepthook):
    oldhook(type, value, traceback)
    print("Looks like you encountered a critcal error")
    print("Check your settings and open a bug report if the issue persists")
    input("Press RETURN to close")


sys.excepthook = exceptionhook


def settings_check(path: str) -> None:
    if os.path.isfile(path):
        print("Found settings")
    else:
        print(f"Could not find PalWorldSettings.ini at {path}")
        input("Press RETURN to close")
        sys.exit(1)


def uesave_check(path: str) -> None:
    if os.path.isfile(path):
        print("Found uesave")
    else:
        print(f"uesave does not exist at {path}")
        input("Press RETURN to close")
        sys.exit(1)


def save_worldoptions(uesave_path: str, worldoption: Dict, output_path: str) -> None:
    print(f"Converting JSON")
    convert_to_save(uesave_path, os.path.join(output_path, "WorldOption.sav.json"), worldoption)


def convert_to_worldoptions(uesave_path: str, settings_file: str, output_path: str) -> None:
    # Make sure files exist
    uesave_check(uesave_path)
    settings_check(settings_file)
    config_settings_json = create_palworldsettings(settings_file)
    save_worldoptions(uesave_path, config_settings_json, output_path)
    print("Complete!")
    print("Restart your palworld server to apply the changes")
    input("Press RETURN to close")


def main() -> None:
    running_dir = os.path.dirname(os.path.realpath(sys.executable if getattr(sys, 'frozen', False) else __file__))
    parser = argparse.ArgumentParser(prog='palworld-worldoptions',
                                     description='Creates a worldoptions.sav file for dedicated servers')
    parser.add_argument('settings_file',
                        default=os.path.join(running_dir, "PalWorldSettings.ini"),
                        help='location of the PalWorldSettings.ini',
                        nargs='?',
                        )
    parser.add_argument('--uesave',
                        default=os.path.join(
                            getattr(sys, '_MEIPASS', os.path.dirname(os.path.realpath(__file__))),
                            "uesave",
                            "uesave.exe"
                        ),
                        help='uesave file location')
    parser.add_argument('--output',
                        default=running_dir,
                        help='output directory for WorldOption.sav')

    args = parser.parse_args()
    convert_to_worldoptions(args.uesave, args.settings_file, args.output)


if __name__ == '__main__':
    main()
