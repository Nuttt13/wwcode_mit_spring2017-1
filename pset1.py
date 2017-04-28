#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 21:12:31 2017

@author: Enund
"""
Part A
annual_salary = int(input('Enter your annual salary: '))
save_per = float(input('Enter the percent of your salary to save, as a decimal: '))
cost_home = int (input('Enter the cost of your dream home: '))

down_payment = cost_home/4
current_savings = 0
r = 0.04
month = 0

monthly_salary = annual_salary/12
monthly_saved = monthly_salary*save_per
while current_savings <= down_payment:
      current_savings += monthly_salary*save_per + current_savings*r/12
      month += 1

print('Number of month: ', month)


Part B
annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = int (input('Enter the cost of your dream home: '))
sami_annual_raise = float(input('Enter your sami annual raise: '))

down_payment = total_cost/4
current_savings = 0
r = 0.04
month = 0
monthly_salary = annual_salary/12

monthly_saved = monthly_salary*portion_saved

while current_savings <= down_payment:
      current_savings += monthly_salary*portion_saved + current_savings*r/12
      month += 1
      if month%6 == 0:
          monthly_salary=monthly_salary+monthly_salary*sami_annual_raise


print('Number of month: ', month)


Part C


sami_annual_raise = .07
r = .04
# r - investments have an annual return
total_cost = 1000000
down_payment = total_cost/4
month =36










