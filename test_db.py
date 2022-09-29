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
    print("employee_id", exec_value[0],)
    print("first_name", exec_value[1],)
    print("last_name", exec_value[2],"\n")
         
#print(executor)           
# conn.commit()            
# conn.close()
# curr.close()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            