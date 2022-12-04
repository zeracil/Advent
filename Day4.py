# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:22:04 2022

@author: matti
"""

print("Please input 1 for case 1: or 2 for Case 2.")
inp = input("input: ")
f = open("Day4input","r")
sum = 0;
for dum in range(1000):
    inputstring = f.readline()
    splitstring = inputstring.split(',');
    interval1 = splitstring[0].split('-');
    interval2 = splitstring[1].split('-');
    interval2[1] = interval2[1].split('\n')[0]
    elf1tasks = set(range(int(interval1[0]),int(interval1[1])+1));
    elf2tasks = set(range(int(interval2[0]),int(interval2[1])+1));
    if inp == "1" and (elf2tasks.issubset(elf1tasks) or elf1tasks.issubset(elf2tasks)):
        sum = sum+1;
    elif inp == "2" and elf1tasks.isdisjoint(elf2tasks):
        sum = sum+1
if inp == "1":
    print("The number of completely overlapping tasks is " + str(sum));
elif inp == "2":
    print("The number of overlapping tasks is " + str(1000-sum));
else:
    print("Invalid input")