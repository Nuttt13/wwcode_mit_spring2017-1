#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 21:12:31 2017

@author: Enund
"""
#num_month = int (input('Number of month: '))
#down_payment = int ()

current_savings = 0
r = 0.04
count = 0
#invest = current_savings*r/12
#down_payment = int(cost_home/4)
#monthly_salary = annual_salary/12


annual_salary = int(input('Enter your annual salary: '))
save_per = float(input('Enter the percent of your salary to save, as a decimal: '))
cost_home = int (input('Enter the cost of your dream home: '))

invest = current_savings*r/12
down_payment = cost_home/4
monthly_salary = annual_salary/12
monthly_saved = monthly_salary*save_per

total_saved = (monthly_saved + invest)
num_month = int(total_saved/down_payment)
print('Number of month: ', num_month)