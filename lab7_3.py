#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def istrue1(s,i):
    b=False
    
    while(i<len(s)):
       
        if(s[i]=='(' or s[i]=='[' or s[i]=='{' or s[i]=='<'):

            
            i+=1
            b=istrue(s,i,i-1)
            
            if(b==False):
                
                return False

        if(i==(len(s)-1)):
            
            return True

        else:
            i+=1
    
def istrue(s,i,b):
    bl=False
    
    while(i<len(s)):
        
        if(s[i]=='(' or s[i]=='[' or s[i]=='{' or s[i]=='<'):
            
            i+=1
            bl=istrue(s,i,i-1)
            
            if(bl==False):
                
                return False
            
            else:
                
                i+=bl
                
        elif(s[i]==')' or s[i]==']' or s[i]=='}' or s[i]=='>'):
            
            if((s[b]=='(' and s[i]==')')or (s[b]=='['and s[i]==']') or (s[b]=='{' and s[i]=='}') or(s[b]=='<' and s[i]=='>')): 

                return i-b

            else:
                
                return False
            
        elif(len(s)==i+1):
            
            return False
        i+=1          
s=input()
if(istrue1(s,0)==True):
    print('True')
else:
    print('False')
