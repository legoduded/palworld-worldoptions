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
- Place your PalWorldSettings.ini into the save directory
- Download palworld-worldoptions.exe from the releases into the save directory
- Run palworld-worldoptions.exe
- Start your server and you're good to go!

Example:

![tutorial](https://private-user-images.githubusercontent.com/16566577/299892843-33ba18d6-fd52-438f-a1a4-a053169bcb27.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDYyNDk3NzgsIm5iZiI6MTcwNjI0OTQ3OCwicGF0aCI6Ii8xNjU2NjU3Ny8yOTk4OTI4NDMtMzNiYTE4ZDYtZmQ1Mi00MzhmLWExYTQtYTA1MzE2OWJjYjI3LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMjYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTI2VDA2MTExOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBkNmM2YTk2Yjc4MWE3MDhkNzg1NGY3NzMxMGVkMjZiNjhlZjAwYjM5YjA2YmU1NjkzMDU1NzE2YzFmZDlkN2YmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.fDICOve7AD7oP4J-Ma9ZuSPNQ7Vc-nh5hS89k4_Mq8c)

## Using the Scripts
The exe should work for most people. If you're running a dedicated linux server you can run the tool via the scripts

Help Dialog
```console
usage: palworld-worldoptions [-h] [--uesave UESAVE] [--save_path SAVE_PATH]

Creates a worldoptions.sav file for dedicated servers

options:
  -h, --help            show this help message and exit
  --uesave UESAVE       specify uesave location
  --save_path SAVE_PATH
                        location of the saved game data folder
```

Example
```console
legoduded@desktop:~/palworld-worldoptions/src/$ python3 main.py --save_path "/mnt/g/pal/SaveGames/0/DDF6BDC891FD4E5DBD8DE895C258C7A8/" --uesave "/home/legoduded/.cargo/bin/uesave"

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
Press RETURN to close
```

## Thanks
Major shout out to cheahjs for creating the inital tool to extract and compress the palworld data
- https://github.com/cheahjs/palworld-save-tools