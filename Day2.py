# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 12:46:53 2022

@author: matti
"""
print("Please input 1 for case 1: or 2 for Case 2.")
inp = input("input: ")
score = 0;
f = open("Day2input","r")
if inp == "1":
    for i in range(2500):
        op = f.read(1);
        f.read(1);
        me = f.read(1);
        f.read(1)
        if (op == "A" and me == "Y") or (op == "B" and me == "Z") or (op == "C" and me == "X"):
            score = score + 6;
        elif (op == "A" and me == "X") or (op == "B" and me == "Y") or (op == "C" and me == "Z"):
            score = score + 3;
        if (me == "X"):
            score = score + 1;
        elif (me == "Y"):
            score = score + 2;
        else:
            score = score + 3;
    print("The final score is: " + str(score) + " points.")
elif inp == "2":
    for i in range(2500):
        op = f.read(1);
        f.read(1);
        res = f.read(1);
        f.read(1)
        if res == "X":
            if op == "A":
                score = score + 3;
            elif op == "B":
                score = score + 1;
            else:
                score = score + 2;
        elif res == "Y":
            if op == "A":
                score = score + 4;
            elif op == "B":
                score = score + 5;
            else:
                score = score + 6;
        else:
            if op == "A":
                score = score + 8;
            elif op == "B":
                score = score + 9;
            else:
                score = score + 7;
    print("The final score is: " + str(score) + " points.")
else:
    print("Invalid input")