#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    param = str(param)[::-1]
    print(re.sub("#g", param, format_string))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
