# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 14:38:08 2021

@author: Athan 
@title Scrumble the words
"""
import random
word = input("Give me the word to scrumble")
wordlen=len(word)
for i in range(40):
    print("scrumbling...")
wordmn = []
for ln in range(0,wordlen):
    wordmn.append(ln)
wordml=[]
for lt in word:
    wordml.append(lt)
wordhidd=[]
for ltrr in range(0,wordlen):
    ranln=random.randint(0,wordlen-1)
    while ranln in wordhidd:
        ranln=random.randint(0,wordlen-1)
    wordhidd.append(ranln)
scrumbledword=[]
for n in wordhidd:
    scrumbledword.append(wordml[n])
i=0
fndwrd=[]
tries=0
for flt in wordml:
    i+=1
    glt=""
    print("found word is:", fndwrd)
    print("scrumbled word is:", scrumbledword)
    print("letter no",i)
    while glt is not flt:
        tries+=1
        glt=input("Guess:")
    fndwrd.append(glt)
    print("success!!!")
print("well done! hidden word was:", word, "and you found it in", tries,"tries. You made", tries-wordlen,"mistakes. Till next time!")
     
