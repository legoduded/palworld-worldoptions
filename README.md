# palworld-worldoptions

A tool for creating WorldOption.sav and applying the PalWorldSettings.ini for dedicated servers
\
\
I also created a web version of this tool: https://palworldoptions.com/

## Background

BaseCampWorkerMaxNum in PalWorldSettings.ini doesn't load on dedicated servers.\
However there is a workaround!\
\
Placing WorldOption.sav with a modified BaseCampWorkerMaxNum in your dedicated server save will apply the configured BaseCampWorkerMaxNum.\
However PalWorldSettings.ini will be ignored!\
This tool will create a WorldOption.sav with your PalWorldSettings.ini applied to it

## Using the EXE
- Shutdown your server
- Drag and drop PalWorldSettings.ini onto the exe or run in the same directory
- Copy WorldOption.sav to your save directory with LevelMeta.sav and Level.sav
- Start your server and check your settings

WorldOption.sav created via the exe can be used for windows and/or linux dedicated servers
\
\
Example:

![tutorial](/assets/example.gif)
\
\
If you want to call the EXE from a script add the `--script` flag to make it non-interactive
## Using the Scripts
The exe should work for most people. If you're running linux you can run the tool via the scripts\
\
Python 3.10 or later\
Linux Users will also need to install uesave
- https://github.com/trumank/uesave-rs

Help Dialog
```console
usage: palworld-worldoptions [-h] [--uesave UESAVE] [--output OUTPUT]
                             [--script]
                             [settings_file]

Creates a worldoptions.sav file for dedicated servers

positional arguments:
  settings_file    location of the PalWorldSettings.ini

options:
  -h, --help       show this help message and exit
  --uesave UESAVE  uesave file location
  --output OUTPUT  output directory for WorldOption.sav
  --script         Don't ask for input when using the exe
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
```

## Thanks
Major shout out to cheahjs for creating the inital tool to extract and compress the palworld data
- https://github.com/cheahjs/palworld-save-tools