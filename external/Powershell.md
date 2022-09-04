Check if user is part of built-in Administrator group:

`(New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)`

Get Powershell version:

`$PSVersionTable.PSVersion`


Robocopy from network drive:

```
NET USE \\RemoteServerName\IPC$ /u:server\user *password* 
robocopy \\Source\ \\RemoteServerName\DestinationDir\ /XD * /Z /MIR /LOG+:c:\temp\log.log
robocopy \\Source C:\dst /E /ZB /MT:8
NET USE \\RemoteServerName\IPC$ /D```
