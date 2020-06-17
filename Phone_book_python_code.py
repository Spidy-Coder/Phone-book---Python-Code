# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 11:02:57 2020

@author: Adesh
"""

import mmap , sys
print("1 to display all the entries")
print("2 to display phone number")
print("3 to modify an entry")
print("4 to exit out of the program")
ch = input("PLEASE PROVIDE YOUR CHOICE FROM 1-4")

if ch=="4":
    sys.exit()
    
with open("phonebook.dat","r+b") as f:
    mm = mmap.mmap(f.fileno(),0)
    
    if ch =="1":
        print(mm.read().decode())
        
    if ch =="2":
        name = input("Enter name:")
        n = mm.find(name.encode())
        n1 = n+len(name)
        ph = mm[n1: n1+10]
        print("Phone no:",ph.decode())
        
    if ch =="3":
        name = input("Enter name:")
        n = mm.find(name.encode())
        n1 = n+len(name)
        ph1 = input("Enter new number:")
        mm[n1: n1+10] = ph1.encode()
        
    mm.close()
    
    