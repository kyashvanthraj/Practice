names = ["amit", "arjun", "amit", "ansh", "ajay", "arjun", "aarav"]

fre_count = {}

for i in names:
    if i in fre_count:
        fre_count[i] += 1 
    else:
        fre_count[i] = 1
    
print(fre_count)

from collections import Counter 
print(Counter(names)) 