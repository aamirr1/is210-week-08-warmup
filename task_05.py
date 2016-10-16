#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 8 Warmup task 5"""

Pressure = raw_input('What is your blood pressure? \n')
Pressure = int(Pressure)

BP_STATUS = None

if Pressure <= 89:
    BP_STATUS = 'Low'
elif 89 < Pressure <= 119:
    BP_STATUS = 'Ideal'
elif 119 < Pressure <= 139:
    BP_STATUS = 'Warning'
elif 139 < Pressure <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

RESULT = 'Your status is currently {}!:'.format(BP_STATUS)

print RESULT
