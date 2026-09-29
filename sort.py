students = [("Ajay",89),
            ("Sujit",78),
            ("Rupesh",65),
            ("Sujal",90)]

def get_marks(students):
    return students[1]
 
# sort using function
print("Using function")
for i in sorted(students, key= get_marks):
    print(i) 

# sort using lambda function
print("Using lambda function")
for i in sorted(students, key = lambda students: (-students[1], students[0])): 
    print(i) 