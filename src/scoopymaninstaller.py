from os import environ, system

print("MAKE SURE YOU ARE RUNNING THIS PYTHON FILE IN AN ELEVATED POEWRSHELL")
system("pause")
# CHECK WHETHER SCOOP IS INSTALLED


def installscoop():
    print("SETTING EXECUTION POLICY, PRESS A WHEN PROMPTED")
    system("Set-ExecutionPolicy RemoteSigned -scope CurrentUser")
    print("INSTALLING SCOOP")
    system("iwr -useb get.scoop.sh | iex")
    print("SCOOP SUCCESSFULLY INSTALLED")

try:
    print(f"SCOOP IS INSTALLED IN {environ['SCOOP']}")
except KeyError:
    print(f"SCOOP IS NOT INSTALLED. INSTALLING SCOOP RIGHT NOW")
    installscoop()

# SCOOP SHOULD INSTALL SUCCESSFULLY

# NOW SETTING UP PACMAN

print("PRESS ANY KEY TO INSTALL pacman.py")
input()
system("pip install wheel nuitka")
system("nuitka src\\pacman.py")
system(f"Copy-Item src\\pacman.exe {environ['SCOOP']}\\shims\\pacman.exe")

print("Cleaning up build files...")
system("Remove-Item python39.dll")
system("Remove-Item pacman.build -Recurse")

# CHECKING IF INSTALLATION WENT SUCCESSFULLY
print("UPDATING AND SETTING UP BASIC APPS")
system("pacman -S 7zip git")
system("pacman -Syu gsudo aria2 grep python")