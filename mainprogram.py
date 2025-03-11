# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 09:56:50 2025

@author: WXH
"""

import csv
with open('6-category.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))