#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    words = format_string.split()

    param = param.swapcase()
    
    for i in range(len(words)):
        if words[i] == "k#":
            words[i] = param
        elif words[i].startswith("#.") and words[i].endswith("k"):
            num = words[i][2:-1]
            if num.isnumeric():
                if int(num) < len(param):
                    str = param[:int(num)]
                    words[i] = str
                else:
                    words[i] = param
        elif words[i].startswith("#") and words[i].endswith("k"):
            num = words[i][1:-1]
            if num.isnumeric():
                str = param.rjust(int(num), ' ')
                words[i] = str
                
    
    print(" ".join(words))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
