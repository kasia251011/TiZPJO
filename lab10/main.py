#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    N = len(str(param))
    F = int((int(param)*2)/N)
    
    if F%2 == 0 :
        print(re.sub("#a", str(F), format_string))
    else:
        HEX = str(hex(int(F)))[2:]
        print(re.sub("#a", HEX, format_string))
    
    

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
