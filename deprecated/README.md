# v0

This version was written for 'nix systems only, it was written I believe originally with python 3.4, so I didn't have the luxury of clean f-string syntax. As a result, I created some pretty weird syntax workarounds (setting a variable to be a `"` character.

After including python libraries for OS commands (e.g `os.mkdir` in lieu of `os.system("mkdir ....")` making it operating system neutral, adding f-strings, and changing a few regex commands to work on only file names (instead of splitting on forward slashes), the newer version is a bit more robust. But I'm keeping this one around for posterity and to reflect on my growth.
