name = "malayalam"

for i in range(len(name)):
    if name[i] == name[len(name)-i-1]:
        print("Palindrome")
        break
    else:
        print("Not a palindrome")
        break 