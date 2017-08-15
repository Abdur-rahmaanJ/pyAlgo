import time
array = [1,3,"a"]
""" 
seqential search
compares one by one element to target to check if target exists

off python, use 
found -> false
while pos < array length && !found
compare array[pos] to target
increase pos by 1
if exist found -> true

ask questions in comments
(c) Abdur-Rahmaan Janhangeer
(c) sololang server #algorithm
"""
def seqS(target,array):
    start = time.clock() #for record
    for item in array: #beauty of py
        if item == target:
            return "found in "+"{0:.20f}".format(time.clock() - start) #float rather than e
    return "not found"  #if did not exit in loop will exit here and so not found
    
print(seqS(1,array))
print(seqS("a",array))
print(seqS(100,array))
