@echo off
Rem Build By LandGrey
title Vpn Traffic Switcher

::get administrator privilege
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (goto UACPrompt) else ( goto gotAdmin )
:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    exit /B
:gotAdmin
    if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
    pushd "%CD%"
    CD /D "%~dp0"

::wait for choosing
:loop
cls
color 8e
echo ************************ Vpn Traffic Switcher ************************
echo.
set /p choice=[*] Input yes or no (y/n):
if %choice%==y (goto enable) else if %choice%==yes (goto enable)
if %choice%==n (goto disable) else if %choice%==no (goto disable) else (goto loop)

:enable
echo.
set /p ipaddress=[*] Input ip range, such as 1.1.1.1 or 1.1.1.1/24 or 1.1.1.1-1.2.3.4: 
netsh advfirewall set domainprofile firewallpolicy blockinbound,blockoutbound
netsh advfirewall set privateprofile firewallpolicy blockinbound,blockoutbound
netsh advfirewall set publicprofile firewallpolicy blockinbound,blockoutbound
netsh advfirewall firewall delete rule name="only_allow_me_connect"
netsh advfirewall firewall add rule name="only_allow_me_connect" dir=out action=allow profile=public,private,domain remoteip=%ipaddress% enable=yes
exit

:disable
echo.
netsh advfirewall set domainprofile firewallpolicy blockinbound,allowoutbound
netsh advfirewall set privateprofile firewallpolicy blockinbound,allowoutbound
netsh advfirewall set publicprofile firewallpolicy blockinbound,allowoutbound
netsh advfirewall firewall delete rule name="only_allow_me_connect"
exit
