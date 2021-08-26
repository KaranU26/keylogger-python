# Keylogger Project

### Compatiblity: Debian/Ubuntu

## Installation Instructions - Antivirus:

1. Go to download location and right click, select "Open in Terminal". Otherwise open a terminal and navigate to download location.
2. Enter the following and press enter: ```chmod +x ./install-ufw```
3. Then the following: ```./install-ufw```. Your password will be requested for the install.
4. Run the antivirus by entering: ```ufw_antivirus```. A notification will pop up to let you know it has started.


## Installation Instructions - FileZilla Server Interface (Windows):
1. Open the link and download the FileZilla server: https://filezilla-project.org/download.php?show_all=1&type=server
2. Run the exe installer
3. Select admin port and remember this port
4. Launch FileZilla Server Interface
5. Enter port from above, enter (new) password for administration, click ok/connect
6. Create a user and/or group with permissions to a home directory.
7. Add additional directory and set the alias name to display within home directory (e.g. /AliasName)
8. Complete

Setup on Windows with built-in firewall: After installation, make sure FileZilla Server is registered as an allowed program to the built-in firewall's allowed programs. In the Control Panel, select System and Security. In Windows Firewall section, choose 'Allowed Programs' to open configuration window. Check both private and public network selection for "FileZilla Server" (Not "FileZilla Server Interface". If "FileZilla Server" is not listed, remember to add "C:\Program Files\FileZilla Server\FileZilla server.exe" or wherever it is installed). If private network is not selected, the incoming FTP connection would be blocked.

### Term Project Submission
This project is a ransomware app that pretends to be an antivirus. It prints messages for the victim to imitate the work of an antivirus. At the same time, it does the keylogging on background and an SFTP client sends a file with logs to the SFTP server. The user gets notifications on start and for scanning. 
We decided to use FileZilla server for implementation of our project. However, we tried to implement an SFTP server and we are submitting its code as well. 
