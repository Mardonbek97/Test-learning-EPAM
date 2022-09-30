# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:06:14 2022

@author: Mardonbek
"""
"This is a test to connect between Python and Postgresql"

import psycopg2 
#from config import config
conn = psycopg2.connect(
    host = "localhost",
    database = "Test_DB",
    user = "postgres",
    password = "sys",
    port="5432")


curr = conn.cursor()
curr.execute("""
            Select emp.employee_id, emp.first_name, emp.last_name 
            from employees as emp
            join
            job_history as job_h
            on emp.employee_id = job_h.employee_id
            where emp.employee_id between 100 and 145
            """)
executor = curr.fetchall()  

for exec_value in executor:
    print("employee_id:", exec_value[0], end = ' ')
    print("first_name:", exec_value[1], end = ' ')
    print("last_name:", exec_value[2],"\n")
         

print(executor)           
conn.commit()             
conn.close()
curr.close()
             
            
            
             
            
import psycopg2 as pg
conn=pg.connect(
                host = 'localhost',
                database = 'Test_DB',
                user = 'postgres',
                password = 'sys',
                port = '5432')
cur = conn.cursor()
cur.execute("""
              Select * from countries
              """)           
                 
sql = cur.fetchall()

for row in sql:
    print(row)
            
            
            
            
            

import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv(r"C:\Users\Mardonbek\Desktop\test.csv")
#df2 = pd.read_csv(r"C:\Users\Mardonbek\Desktop\test2.csv")


plt.pie(df)

plt.show()


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 5, 4, 8])
ypoints = np.array([3, 8, 1, 7])

plt.plot(xpoints, xpoints)
plt.show()


import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('Solarize_Light2')
df = pd.read_csv(r"C:\Users\Mardonbek\Desktop\test.csv")


x=df.get('country', default='no_country')
y=df.get('value_counts', default='no_value')


plt.xlabel('Country', fontsize=20)
plt.ylabel('value_counts', fontsize=20)
plt.bar(x, y)

plt.show()
























 




            
            
            