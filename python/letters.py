#!/bin/env python3
letters = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s","t", "u", "v", "w", "x", "y", "z"]
values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
lettermap = {}

for i in values:
#    print (letters[i] + ':' + str(i))
    lettermap[letters[i]] = i
while True:
    word = input("Enter a word (Q to Quit):" )
    if word == "Q":
        break
    else: 
#        print (word)
        summation = 0
        for letter in word:
            summation += lettermap[letter]

        print (word + "=" + str(summation))
