#!/usr/bin/env python3

#name = 'Jon'
#age = 20
#print('Hi ' + name + ', you are ' + str(age) + ' years old.')

#colour = input("Type in a colour and press enter: ")
#print(colour)
#print('The colour I typed in is: ' + colour)

#name = input("Name: ")
#age = input("Age: ")
#print('Hi ' + name + ', you are ' + str(age) + ' years old.')
import sys

if len(sys.argv) != 3:
    print('Usage: ' + sys.argv[0] + ' name age')
    sys.exit()



name = sys.argv[1]
age = int(sys.argv[2])
print('Hi ' + name + ', you are ' + str(age) + ' years old.')
