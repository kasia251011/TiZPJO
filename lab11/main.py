#!/usr/bin/env python3

import sys

def convert(number):
    res = bin(number)[2:]
    res = res[::-1]
    res_list = list(res)
    
    tab = 'abcdefghij'
    tab_index = 0
    
    for i in range(len(res)):
        letter = tab[tab_index]
        if res_list[i] == '1':
            res_list[i] = letter
        tab_index += 1
        if tab_index == 10:
            tab_index = 0
    res = ''.join(res_list)
    res = res[::-1]
    return res

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                print(param,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
