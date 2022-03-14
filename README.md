# dbloat
*Python ADB Android debloating script.*
<br><br>

<p align="center">  
    <img width="772" src="https://i.imgur.com/ZIbHz4t.png">
</p><br>

## Disclaimer
The packages included for removal with this script have been deemed **SAFE TO REMOVE** by the community. 

Still, keep in mind that removing system apps with ADB using this script or by other means **may lead to data loss** and **render your device unbootable** if done incorrectly.

Proceed ***at your own risk***!
<br><br>

## Prerequisites
1. Install [ADB](https://developer.android.com/studio/command-line/adb) 
    - Ubuntu / Debian:<br>
    ```sudo apt install android-tools-adb```
    - For other OS, follow [this guide](https://www.xda-developers.com/install-adb-windows-macos-linux/).
2. Enable USB debugging: 'Settings > Developer options > USB debugging'.
3. Connect your device to the computer using a USB cable.
<br><br>

## Installation and Usage
To download and use this script, open a terminal (CTRL + T) and execute the following commands:
```
git clone https://github.com/Julynx/dbloat
```
```
cd dbloat
```
```
python3 dbloat.py
```
<br>

## Advanced Features
This script comes with options to remove MIUI Bloatware, Google Bloatware, and more. The included files are mostly suited for debloating a Xiaomi phone, but you can easily add packages to the debloat lists or create a new one for your phone model.

If you want to add packages to debloat, write the name of each package line by line in a ```.txt``` file inside the ```dbloat``` directory. It will show up as an option the next time you run the ```dbloat.py``` script. 

You can search for packages considered 'bloatware' for your smartphone model in the [XDA forums](https://www.xda-developers.com/).

If you want to reinstall or get back an uninstalled app, you can do it by executing:
```
adb shell cmd package install-existing <package_name>
```

