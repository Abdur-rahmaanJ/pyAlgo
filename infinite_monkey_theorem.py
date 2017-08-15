#solving the infinite monkey theorem
#visit abdurrahmaanjanhangeer.wordpress.com

import random
phrase = "i" 
#set to i if too long 
#on your pc set to like "you are watching"

alph=list("abcdefghijklmnopqrstuvwxyz ")

myphrase=""

trial=0
while phrase != myphrase:
    myphrase=""    
    for i in range(len(phrase)):
        x =random.randint(0,26)
        myphrase=myphrase+alph[x]
    print(trial,myphrase)
    trial+=1
    
print('found',myphrase,'=',phrase)
        
    
"""
if a monkey types randomly, can he finish with complete works ? if so, after how much time ?
"""
