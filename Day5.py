# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:10:54 2022

@author: matti
"""

print("Please input 1 for case 1: or 2 for Case 2.")
inp = input("input: ")
f = open("Day5input","r")
stacks = [[],[],[],[],[],[],[],[],[]];
for i in range(8):
    for j in range(9):
        f.read(1);
        dummy = f.read(1);
        if dummy != " ":
            stacks[j].insert(0,dummy);
        f.read(2);

f.readline()
f.readline()
if inp == "1":
    for lines in f:
        lines = lines.strip();
        lines = lines.split(" ");
        numtomove = int(lines[1]);
        fromstack = int(lines[3])-1;
        tostack = int(lines[5])-1;
        for k in range(numtomove):
            stacks[tostack].append(stacks[fromstack].pop(len(stacks[fromstack])-1));
    print("The top of the stacks from stack 1 to stack 9: ")
    stacktops = "";
    for i in range(9):
        stacktops = stacktops + stacks[i][len(stacks[i])-1]
    print(stacktops)
elif inp == "2":
    for lines in f:
        lines = lines.strip();
        lines = lines.split(" ");
        numtomove = int(lines[1]);
        fromstack = int(lines[3])-1;
        tostack = int(lines[5])-1;
        movedboxes = stacks[fromstack][len(stacks[fromstack])-numtomove:len(stacks[fromstack])];
        stacks[tostack].extend(movedboxes);
        for k in range(numtomove):
            stacks[fromstack].pop(len(stacks[fromstack])-1);
    print("The top of the stacks from stack 1 to stack 9: ")
    stacktops = "";
    for i in range(9):
        stacktops = stacktops + stacks[i][len(stacks[i])-1]
    print(stacktops)
else:
    print("Invalid input")
            
    
    
    
    