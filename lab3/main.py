#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):

    param = param.swapcase()
    
    x = re.search("#\.\d+k", format_string)
    
    if x:
        format = x.group()
       	num = format[2:-1]
        if num.isnumeric():
          if int(num) < len(param):
            str = param[:int(num)]
            x = re.sub("#\.\d+k", str, format_string)
            print(x)
            return
          else:
            str = param[:int(num)]
            x = re.sub("#\.\d+k", str, format_string)
            print(x)
            return
    x = re.search("#\d+k", format_string)
    
    if x:
        format = x.group()
       	num = format[1:-1]
        if num.isnumeric():
          str = param.rjust(int(num), ' ')
          x = re.sub("#\d+k", str, format_string)
          print(x)
          return
    x = re.search("#k", format_string)
    
    print(re.sub("#k", param, format_string))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
