# GUC-System-Opener
simple python script to open cms , mail and portal with 1 click
# Requirments :
Install [Google Chrome](https://www.google.com/chrome/) , if you changed the default installation directory update your chrome.exe path in the .env file <br /><br />
Google chrome is the default browser , you can change it in the .env file with you preferable browser.exe
# How to run :
```bash
git clone https://github.com/M-Bahy/GUC-System-Opener.git
cd GUC-System-Opener
pip install -r  requirements.txt
```
executable program avilable in the release section (Only supporting chrome in its default path) 
# Additional command :
If you changed the .env file then you need to run this command in the same terminal of the above commands
```bash
pyinstaller -F -w -i icon.ico GUC.py
```
⚠️ Disable you antivirus before running this command as some antivirus interupt with it <br /><br />
The new GUC.exe will be in the folder called "dist" , create a shortcut for it on your desktop
