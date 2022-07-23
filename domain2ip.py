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

# ---------------------------------------------------------------------------
# CODE
# ---------------------------------------------------------------------------

# Functions


# ask for the input file path
try:
    f = open(input('Type in your file path: '), "r")
except:
        print("Reading File ERROR!");

domain_list = f.read()
if ("https://" or "http://" or "/" in domain_list):
    domain_list = domain_list.replace("https://","")
    domain_list = domain_list.replace("http://","")
    domain_list = domain_list.replace("/","")
domain_list = domain_list.split('\n')

for domain  in domain_list:
    try:
        # print(domain) DEBUG only
        output = socket.gethostbyname(domain)
        print(output)
    except:
        print("ERROR!");
f.close()
