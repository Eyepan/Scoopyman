# Scoopyman
This is a PACMAN like wrapper for SCOOP package manager written in Python in Windows 10. 

Please check out my C++ scoopman repo from https://github.com/Eyepan/scoopman since it is the most updated.
And please check out PACAPTR https://github.com/rami3l/pacaptr which is written in Rust, and honestly is coded better than me

That being said follow these instructions if you still want to use this
# MAKE SURE YOU ARE RUNNING AS AN ADMIN TO USE THE INSTALL SCRIPT

# INSTALL INSTRUCTIONS
Open up an Elevated Powershell by Pressing Win + X and then A

`cd` to any directory of your wish

`git clone https://github.com/Eyepan/Scoopyman.git`

`cd Scoopyman`

`Set-ExecutionPolicy RemoteSigned -scope CurrentUser`

`.\scoopyinstaller.ps1`

And follow the instructions which appear on your screen and you are done! Enjoy using `sudo pacman -Syu` when installing apps in Windows

# NOTE

All apps are installed globally by default. To disable this go into `src/pacman.py` and uncomment line 7 which says 

`#globally = ''`

`.\scoopyinstaller.ps1` again

And have fun!

# USAGE INSTRUCTIONS

|Flags|Use Case|Scoop Equivalent|
|-----|--------|----------------|
|-(or) -h| Show this page|`scoop help`|
|-S|Install an/multiple apps|`scoop install`|
|-Syu|Update all installed apps and install additional apps if necessary|`scoop update * && scoop install`|
|-Q|List all installed apps|`scoop list`|
|-Qe|Search for installed apps|`scoop which`|
|-Ss|Searches online for apps|`scoop search`|
|-R|Removes/Uninstalls an app|`scoop uninstall`|
|Anything else|Invalid option|`scoop help`|

I can add any and all functionality that is required. Feel free to raise an issue!
