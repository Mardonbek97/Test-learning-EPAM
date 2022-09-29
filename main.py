# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:24:53 2022x`

@author: Mardonbek
"""

import cx_Oracle

dsn = cx_Oracle.makedsn('localhost', '8080', 'xe')
connection = cx_Oracle.connect('Mardonbek', '9799', dsn)
cursor = connection.cursor()  