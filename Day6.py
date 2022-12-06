# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 18:38:10 2022

@author: matti
"""

print("Please input 1 for case 1: or 2 for Case 2.")
inp = input("input: ")
f = open("Day6input","r");
if inp == "1":
    a = [];
    for dum in range(4):
        a.append(f.read(1));
    notFound = True;
    counter = 4;
    while notFound:
        notFound = False
        if a[0] == a[1] or a[0] == a[2] or a[0] == a[3]:
            notFound = True;
        elif a[1] == a[2] or a[1] == a[3]:
            notFound = True;
        elif a[2] == a[3]:
            notFound = True;
        if notFound == True:
            a[0] = a[1];
            a[1] = a[2];
            a[2] = a[3];
            a[3] = f.read(1);
            counter = counter + 1;
    print("Number of processed characters before start-of-packet marker: " + str(counter)  );
if inp == "2":
    a = [];
    for dum in range(14):
        a.append(f.read(1));
    notFound = True;
    counter = 14;
    while notFound:
        notFound = False;
        for i in range(14):
            if a.count(a[i]) > 1:
                notFound = True;
        if notFound == True:
            for j in range(13):
                a[j] = a[j+1];
            a[13] = f.read(1);
            counter = counter + 1;
    print("Number of processed characters before start-of-message2 marker: " + str(counter)  );
            
