#!/bin/bash

sudo yum -y update

sudo yum -y install python3

sudo pip3 install --upgrade pip

sudo yum -y install python3 python3-pip

#Installing the required libraries
sudo yum -y install python3-tkinter
sudo pip3 install paramiko

#installing the GNOME graphical interface requires restarting the system
yum -y groupinstall "GNOME Desktop" "Graphical Administration Tools"
ln -sf /lib/systemd/system/runlevel5.target /etc/systemd/system/default.target

echo 'perform a reboot as soon as you are ready'
