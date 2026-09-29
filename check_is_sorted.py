marks = [10,20,30,40]   

flag = False
for i in range(len(marks)-1):
    if marks[i] > marks[i+1]:
        flag = True
        break
    else:
        flag = False 

if flag:
    print("The list is not sorted")
else:
    print("The list is sorted")  
