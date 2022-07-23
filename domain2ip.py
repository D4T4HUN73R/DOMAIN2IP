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


# ---------------------------------------------------------------------------
# CODE
# ---------------------------------------------------------------------------

# read the input file
domain_list_path = input('Enter the domain list filename or path: ')

f = open(domain_list_path, 'r', encoding='utf-8')
content = f.read()
print(content)

