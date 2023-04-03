#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    list1 = list(param)
    for i in range(len(list1)):
        if list1[i] == '0':
            list1[i] = '9'
        else:
            list1[i] = str(int(list1[i]) - 1)
    param = ''.join(list1)

    x = re.search("#\d+g", format_string)
    if x:    
        format = x.group()
        num = format[1:-1]
        if num.isnumeric():
            s = param.rjust(int(num), ' ')
            x = re.sub("#\d+g", s, format_string)
            print(x)
            return
    print(re.sub("#g", param, format_string))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
