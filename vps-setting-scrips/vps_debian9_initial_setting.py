# -*- coding: utf-8 -*-
"""
    vps_debian9_initial_setting.py
    ~~~~~~~~~
    vps上Debian9的初始设定脚本.
"""
import os
import sys
import subprocess
import shlex

HOSTNAME = 'joycenow'


#: 1.software update
#: 2. set hostname
#: 3. set time zone
def initial_setting(hostname=None, time_zone=None):
    install_software_update = 'apt-get update && apt-get upgrade'
    res_update = os.system(install_software_update)
    if not res_update:
        hostname_set = 'hostnamectl set-hostname ' + hostname
        os.system(hostname_set)
    else:
        print('Errors happened processing apt-get update ')
    timezone_set = 'echo ' + time_zone + '> /etc/timezone' + \
                   '&& ln -fs /usr/share/zoneinfo/`cat /etc/timezone` /etc/localtime'
    os.system(timezone_set)
    check_timezone_set = 'dpkg-reconfigure -f noninteractive tzdata'
    os.system(check_timezone_set)


def add_limited_user(username=None, passwd=None):
    res_useradd = os.system('bash ./useradd_script.sh ' + username + ' ' + passwd)
    if not res_useradd:
        os.system('adduser ' + username + ' sudo')
    else:
        print('adduser ' + username + ' Failed.')





