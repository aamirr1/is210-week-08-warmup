#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 8 Warmup task 4 (A single if statement)."""

MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LONGSTR = 'short'

# You code goes here
INPUT_LENGTH = len(MYINPUT)

if INPUT_LENGTH > MAX_LENGTH:
    LONGSTR = 'long'
else:
    LONGSTR = 'short'

RESULT = 'That certainly was a {} story!'.format(LONGSTR)

print RESULT
