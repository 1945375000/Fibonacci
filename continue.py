#!/usr/bin/env python3
while True:
    n=int(input("Please enter an Integer: "))
    if n<0:
        break
    elif n==0:
        continue
    print("Square is ",n**2)
print("Goodbye")
