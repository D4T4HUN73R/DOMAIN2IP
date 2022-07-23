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
def readFile(domain_list_path):
    file_content = open(domain_list_path, "r")
    domain_array = file_content.read().splitlines()
    file_content.close()
    return domain_array

# ask for the input file paht
domain_list_path = input('Enter the domain list filename or path: ')

domain_array = readFile(domain_list_path)






f = open(domain_list_path, 'r', encoding='utf-8')
hostname_list = f.read()

ip_addresses = socket.gethostbyname(hostname_list)
print(ip_addresses)
