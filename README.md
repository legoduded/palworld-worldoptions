# palworld-worldoptions

A tool for creating WorldOption.sav and applying the PalWorldSettings.ini for dedicated servers

## Background

BaseCampWorkerMaxNum in the PalWorldSettings.ini doesn't seem to load into dedicated servers.
However there is a workaround! Using the WorldOption.sav the server will ignore PalWorldSettings.ini and load the 
server settings from WorldOption.sav which will apply the BaseCampWorkerMaxNum. But since PalWorldSettings.ini is
ignored, I created this tool to help others running dedicated servers migrate their configs into WorldOption.sav

## Requirements
Python 3.10 or later

Linux Users will also need to install uesave
- https://github.com/trumank/uesave-rs

## Usage

Place your PalWorldSettings.ini into the same directory as your dedicated server save and run the script.

```console
python3 main.py <save_path>

positional arguments:
  save_path        location of the saved game data folder

options:
  -h, --help       show this help message and exit
  --uesave UESAVE  specify uesave location
```

Example:

```console
python3 main.py G:\pal\SaveGames\0\DDF6BDC891FD4E5DBD8DE895C258C7A8

Found game files
Found uesave
Converting G:\pal\SaveGames\0\DDF6BDC891FD4E5DBD8DE895C258C7A8\LevelMeta.sav to JSON (using C:\Users\legod\PycharmProjects\palworld-worldoptions\uesave\uesave.exe)

Loading JSON
Writing JSON to G:\pal\SaveGames\0\DDF6BDC891FD4E5DBD8DE895C258C7A8\LevelMeta.sav.json
Loading JSON from G:\pal\SaveGames\0\DDF6BDC891FD4E5DBD8DE895C258C7A8\WorldOption.sav.json
Converting JSON

Converted G:\pal\SaveGames\0\DDF6BDC891FD4E5DBD8DE895C258C7A8\WorldOption.sav.json to G:\pal\SaveGames\0\DDF6BDC891FD4E5DBD8DE895C258C7A8\WorldOption.sav
Cleaning up
Complete!
Restart your palworld server to apply the changes
```

Restart your server and you're good to go!


Linux users will need to install uesave and specify the location

```
$ python3 main.py "/mnt/g/pal/SaveGames/0/DDF6BDC891FD4E5DBD8DE895C258C7A8/" --uesave "/home/legoduded/.cargo/bin/uesave"

Found game files
Found uesave
Converting /mnt/g/pal/SaveGames/0/DDF6BDC891FD4E5DBD8DE895C258C7A8/LevelMeta.sav to JSON (using /home/legoduded/.cargo/bin/uesave)

Loading JSON
Writing JSON to /mnt/g/pal/SaveGames/0/DDF6BDC891FD4E5DBD8DE895C258C7A8/LevelMeta.sav.json
Loading JSON from /mnt/g/pal/SaveGames/0/DDF6BDC891FD4E5DBD8DE895C258C7A8/WorldOption.sav.json
Converting JSON

Converted /mnt/g/pal/SaveGames/0/DDF6BDC891FD4E5DBD8DE895C258C7A8/WorldOption.sav.json to /mnt/g/pal/SaveGames/0/DDF6BDC891FD4E5DBD8DE895C258C7A8/WorldOption.sav
Cleaning up
Complete!
Restart your palworld server to apply the changes
```

## Thanks
Major shout out to cheahjs for creating the inital tool to extract and compress the palworld data
- https://github.com/cheahjs/palworld-save-tools