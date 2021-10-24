# GeigerLog

Python Scipts that reads data from GQ Geiger Muller Counters over Serial

Scripts can be used push data to Home Assistant by using the "command_line" integration and adding it to your configuration.yaml file

See [sample.yaml](https://github.com/lachlanalston/GeigerLog/sample.yaml)

## Devies
Tested with:
* GMC-320+ V5

## Known Issues

| Issue                                                                | Fix            |
|----------------------------------------------------------------------|----------------|
|BRLTTY stops CH340/CH341 usb serial devices from being mounted in /dev|Uninstall BLRTTY|

