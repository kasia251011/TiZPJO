#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    param = str(hex(int(10)))[2:]
    param = param.replace("a","g")
    param = param.replace("b","h")
    param = param.replace("c","i")
    param = param.replace("d","j")
    param = param.replace("e","k")
    param = param.replace("f","l")
    x = re.sub("#j", param, format_string)
    print(x)

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
