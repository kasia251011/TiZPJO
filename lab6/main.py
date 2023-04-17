#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    x = re.search("#\.\d+g", format_string)
    param = str(param)
    if x:    
        format = x.group()
        num = format[2:-1]
        s = param.rjust(int(num), ' ')
        x = re.sub("#\.\d+g", s, format_string)
        print(x)
        return
    print(format_string)

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
