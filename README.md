# palworld-worldoptions

A tool for creating WorldOption.sav and applying the PalWorldSettings.ini for dedicated servers

## Background

BaseCampWorkerMaxNum in the PalWorldSettings.ini doesn't seem to load into dedicated servers.
However there is a workaround! Using the WorldOption.sav the server will ignore PalWorldSettings.ini and load the 
server settings from WorldOption.sav which will apply the BaseCampWorkerMaxNum. But since PalWorldSettings.ini is
ignored, I created this tool to help others running dedicated servers migrate their configs into WorldOption.sav

## Requirements
### Running Via EXE
Just drop it into your save file

### Running Via Python

Python 3.10 or later
Linux Users will also need to install uesave
- https://github.com/trumank/uesave-rs

## Using the EXE

- Shutdown your server
- Drag and drop PalWorldSettings.ini onto the exe or run in the same directory
- Copy WorldOption.sav to your save directory with LevelMeta.sav and Level.sav
- Start your server and check your settings

Example:

![tutorial](/assets/example.gif)
## Using the Scripts
The exe should work for most people. If you're running a dedicated linux server you can run the tool via the scripts

Help Dialog
```console
usage: palworld-worldoptions [-h] [--uesave UESAVE] [--output OUTPUT]
                             [settings_file]

Creates a worldoptions.sav file for dedicated servers

positional arguments:
  settings_file    location of the PalWorldSettings.ini

options:
  -h, --help       show this help message and exit
  --uesave UESAVE  uesave file location
  --output OUTPUT  output directory for WorldOption.sav
```

Example
```console
legoduded@desktop:~/palworld-worldoptions/src$ python3 main.py /mnt/g/PalServer/Pal/Saved/Config/WindowsServer/PalWorldSettings.ini --uesave ~/.cargo/bin/uesave --output /mnt/g/PalServer/Pal/Saved/SaveGames/0/8FAEE1FC44A4A5032BC92F8BCFD43AE3
Found settings
Found uesave
Converting JSON

Converted /mnt/g/pal/steamcmd/steamapps/common/PalServer/Pal/Saved/SaveGames/0/8FAEE1FC44A4A5032BC92F8BCFD43AE3/WorldOption.sav.json to /mnt/g/pal/steamcmd/steamapps/common/PalServer/Pal/Saved/SaveGames/0/8FAEE1FC44A4A5032BC92F8BCFD43AE3/WorldOption.sav
Complete!
Restart your palworld server to apply the changes
Press RETURN to close
```

## Thanks
Major shout out to cheahjs for creating the inital tool to extract and compress the palworld data
- https://github.com/cheahjs/palworld-save-tools