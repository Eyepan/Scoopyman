function installscoop()
{
    Invoke-WebRequest -useb get.scoop.sh | Invoke-Expression
    [System.Environment]::SetEnvironmentVariable('SCOOP',"$env:HOME\scoop",[System.EnvironmentVariableTarget]::User)
}

Write-Output "I hope you have enabled Set-Executive policy as RemoteSigned to Current user"
Write-Output "If not you have to copy and paste this next line in an Elevated Powershell window (Powershell running as admin)"
Write-Output "Set-ExecutionPolicy RemoteSigned -scope CurrentUser"
$Choice = Read-Host -Prompt "Are you running this script in an Elevated Powershell window? (Y/N)"
if (($Choice -eq "N") -OR ($Choice -eq "n"))
{
    exit
}
elseif (($Choice -eq "Y") -OR ($Choice -eq "y"))
{
    Write-Output "Good then, Let's proceed with setting up SCOOP first..."
}
else
{
    Write-Output "INVALID ANSWER"
    exit
}


Write-Output "Checking if SCOOP has already been installed..."
try {
    scoop which scoop
}
catch {
    Write-Output "SCOOP is not installed"
    installscoop
}

Write-Output "SCOOP INSTALLED IN DIRECTORY $env:SCOOP"

# finally starting to setup pacman

Write-Output "Installing pacman..."
pip install wheel pyinstaller
pyinstaller src\pacman.py
Copy-Item dist\pacman\pacman.exe $env:SCOOP\shims\pacman.exe
Write-Output "Cleaning up build files..."
Remove-Item build -Recurse
Remove-Item src\__pycache__ -Recurse
Remove-Item pacman.spec
Remove-Item dist -Recurse
pacman -S 7zip git
pacman -Syu gsudo aria2 grep