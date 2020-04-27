# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:37:17 2019

@author: User-PC
"""
#Problem set 1 Problem 1 

count=0

for x in s:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        count+=1
print("Number of vowels: "+str(count))

#Problem set 1 Problem 2 

count=0
tracker=0

for x in s:
    tracker+=1
    if x=="b":
        if s[tracker:tracker+1]=="o" and s[tracker+1:tracker+2]=="b":
            count+=1
print("Number of times bob occurs is: " +str(count))

#Problem set 1 Problem 3

count=0
subcount=0
tracker=-1
stracker=169
phrase="yo"
alpha="abcdefghijklmnopqrstuvwxyz"
dalpha=0

for x in s:
    #should reset everything to start again from the next letter in s
    tracker+=1
    stracker=tracker
    subcount=0
    dalpha=0
    #Iterating for each letter hopefully
    while dalpha<26:
        while s[stracker:stracker+1]==alpha[dalpha:dalpha+1]==False and dalpha<26:
            dalpha+=1
        while s[stracker:stracker+1]==alpha[dalpha:dalpha+1] and dalpha<26:
            subcount+=1
            stracker+=1
        dalpha+=1    
    if subcount>count:
        count=subcount
        phrase=s[tracker:tracker+count]
print("Longest substring in alphabetical order is: "+phrase)