## osu! Background Changer

A simple tool for automatically changing all your osu! beatmap backgrounds
to a custom one. When replacing, it loops trough all your beatmaps and makes a backup
of the original background (with a .bak extension). If you happen to remove it, you will be stuck with your custom background, unable to recover the original one. If the backup succeeded, it will attemt to replace the original background with your custom one. When recovering, it simply checks if there's a .bak file in the directory, deletes the custom background and removes the .bak extension on the backup. For the sake of simplicity, place both the script and the desired background in the osu!/songs folder. This is only to avoid having to set a custom path for the image.

Use at your own risk.


### Downloads
Windows Binaries (x86-x64) can be found here: 
* https://drive.google.com/file/d/0B0gjiklZC-ivcHd0OTJ3T0RXZDA