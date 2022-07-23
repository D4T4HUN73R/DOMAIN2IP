#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By : TheDataHunter - https://github.com/TheDataHunter
# Created Date : 23/07/2022
# version ='1.0'
# status : RFU (ready for use)
# license : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
# copyrights : 
# ---------------------------------------------------------------------------
""" A simple Python script that looks up your Domain lists and outputs the matching IP addresses to another list. """
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import socket
import os
# ---------------------------------------------------------------------------
# CODE
# ---------------------------------------------------------------------------

# Functions

# INPUT

try:
    origin_path = input('Type in your file path: ')
    file_path = os.path.dirname(os.path.realpath(origin_path))
    print(file_path)
    f = open(origin_path, "r")
except:
        print("Reading File ERROR!");

domain_list = f.read()
if ("https://" or "http://" or "/" in domain_list):
    domain_list = domain_list.replace("https://","")
    domain_list = domain_list.replace("http://","")
    domain_list = domain_list.replace("/","")
domain_list = domain_list.split('\n')

# GET IP
for domain in domain_list:
    try:
        output = socket.gethostbyname(domain)
        
        # OUTPUT
        file_name = 'ip_list.txt'
        with open (file_path + "/" + file_name, 'a') as f:
            f.write(output + '\n')
    except:
        print("ERROR!");
f.close()
print("Your IP-List has succcessfully been generated!")
