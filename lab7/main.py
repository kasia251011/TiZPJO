#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    param = hex(param)
    x = re.sub("#j", s, format_string)
    print(x)

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
