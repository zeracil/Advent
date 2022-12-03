# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:53:55 2022

@author: matti
"""

f = open("Day3input", "r")
sum = 0;
print("Please input 1 for case 1: or 2 for Case 2.")
inp = input("input: ")
if inp == "1":
    for line in f:
        length = len(line);
        halfLength = int(length/2);
        rs1 = line[0:halfLength];
        rs2 = line[halfLength:length-1];
        rss1 = sorted(rs1);
        rss2 = sorted(rs2);
        found = False;
        for obj in rss1:
            for i in range(halfLength):
                if obj == rss2[i]:
                    dup = obj;
                    found = True;
                    break;
                elif rss2[i] > obj:
                    break;
            if found:
                break;
        if dup < "a":
            sum = sum+ord(dup)-38;
        else:
            sum = sum+ord(dup)-96;
    print("The sum of the item priorities is: " + str(sum) + ".")
elif inp == "2":
    for dum in range(100):
        rs1 = f.readline();
        length1 = len(rs1);
        rss1 = sorted(rs1[0:length1-1]);
        rs2 = f.readline();
        length2 = len(rs2);
        rss2 = sorted(rs2[0:length2-1]);
        rs3 = f.readline()
        length3 = len(rs3);
        rss3 = sorted(rs3[0:length3-1]);
        found = False;
        for obj in rss1: 
            for i in range(length2-1):
                if obj == rss2[i]:
                    for j in range(length3-1):
                        if obj == rss3[j]:
                            dup = obj;
                            found = True;
                            break;
                        elif rss3[j] > obj:
                            break;
                elif rss2[i] > obj:
                    break;
                elif found:
                    break;
            if found:
                break;
        if dup < "a":
            sum = sum+ord(dup)-38;
        else:
            sum = sum+ord(dup)-96;
    print("The sum of the item priorities is: " + str(sum) + ".");
        