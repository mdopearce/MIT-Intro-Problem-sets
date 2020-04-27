# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:30:09 2019

@author: User-PC
"""
#####
"""
mistaken code piece, could be useful though
"""

def isLetterGuessed1(secretWord, lettersGuessed):
    check=0
    for range in lettersGuessed:
        if range in secretWord==False:
            return False
        else:
            check+=1
    return check==len(secretWord)
####

"""
problem 1
"""
def isWordGuessed(secretWord, lettersGuessed):
    sword=[]
    for letter in secretWord:
        sword.append(letter)
    for check in lettersGuessed:
        while check in sword:
            sword.remove(check)
    if len(sword)==0:
        return True
    else:
        return False
    
"""
problem 2
"""    
def getGuessedWord(secretWord, lettersGuessed):
    sword=[]
    printout=[]
    for letter in secretWord:
        sword.append(letter)
    for check in sword:
        n=0
        for letter in lettersGuessed:
            if check==letter:
                n+=1
        if n>=1:
            printout.append(check+' ')
        else:
            printout.append('_ ')     
    return ''.join(printout)

"""
Problem 3
"""
def getAvailableLetters(lettersGuessed):
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for k in a:
        if k in lettersGuessed:
            a.remove(k)
    return ''.join(a)
    
"""
Problem 4
"""    


    
    
    




