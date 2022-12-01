# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:30:14 2022

@author: matti
"""
print("Please input 1 for case 1: one elf (with most calories) or 2 for Case 2: three elves (with most calories)")
inp = input("input: ")
if inp == "1":
    # Part 1
    f = open("Day1input", "r")
    largest = 0;
    linelist = [];
    for line in f:
        if line == '\n':
            set = sum(linelist);
            if set > largest:
                largest = set;
            linelist = [];
        else:
            linelist.append(int(line))
    print("The elf that is carrying the most calories, carries " + str(largest) + " calories.")

# Part 2
elif inp == "2":
    f = open("Day1input", "r")
    largest = [0,0,0]
    linelist = [];
    for line in f:
        if line == '\n':
            set = sum(linelist);
            if set > largest[0]:
                largest[2] = largest[1];
                largest[1] = largest[0];
                largest[0] = set;
            elif set > largest[1]:
                largest[2] = largest[1];
                largest[1] = set;
            elif set > largest[2]:
                largest[2] = set;
            linelist = [];
        else:
            linelist.append(int(line))
    print("The three elves that are carrying the most calories, carry " + str(sum(largest)) + " calories together.")
else:
    print("Invalid input")