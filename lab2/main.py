#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    shouldDo2=True
    shouldDo3=True
    for idx in range(0,len(format_string)):
        if shouldDo and shouldDo2 and shouldDo3:
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                param = param.swapcase()
                print(param,end="")
                shouldDo=False
            elif format_string[idx] == '#' and format_string[idx+1] == '.' and format_string[idx+2].isnumeric() and format_string[idx+3] == 'k':
                param = param.swapcase()
                param = param.rjust(int(format_string[idx+2]), ' ')
                print(param,end="")
                shouldDo=False
                shouldDo2=False
                shouldDo3=False
            else:
                print(format_string[idx],end="")
        else:
            if shouldDo2 == True:
                shouldDo3 = True
            if shouldDo == True:
                shouldDo2 = True
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
