# Scoopyman
This is a PACMAN like wrapper for SCOOP package manager written in Python in Windows 10. 

# MAKE SURE YOU ARE RUNNING AS AN ADMIN TO USE THE INSTALL SCRIPT

# INSTALL INSTRUCTIONS
Open up an Elevated Powershell by Pressing Win + X and then A
`cd` to any directory of your wish

`git clone https://github.com/Eyepan/Scoopyman.git`

`cd Scoopyman`

`.\scoopyinstaller.ps1`

And follow the instructions which appear on your screen and you are done! Enjoy using `sudo pacman -Syu` when installing apps in Windows

# NOTE

All apps are installed globally by default. To disable this go into `src/pacman.py` and uncomment line 7 which says 

`#globally = ''`

And have fun!
