print("===== STUDENT REPORT =====")
students = [["Alice", 85, 90, 78], ["Bob", 70, 88, 92], ["Charlie", 95, 80, 89], ["David", 60, 75, 68],
            ["Eva", 88, 92, 95], ["Frank", 72, 65, 80], ["Grace", 90, 85, 91]
]

for i in students:
    avg = (i[1] + i[2] + i[3]) / 3
    i.append(avg)

print(f"Alice avg : {students[0][4]:.2f}")
print(f"Bob avg : {students[1][4]:.2f}")
print(f"Charlie avg : {students[2][4]:.2f}")
print(f"David avg : {students[3][4]:.2f}")
print(f"Eva avg : {students[4][4]:.2f}")
print(f"Frank avg : {students[5][4]:.2f}")
print(f"Grace avg : {students[6][4]:.2f}")


if i[4] >= 80:
    i.append(students[5]) 
    print(f"Top Students : {students[0][0]}, {students[1][0]}, {students[2][0]}, {students[4][0]}, {students[6][0]}")  


if students[0][1] < 70 or students[1][1] < 70 or students[2][1] < 70 or students[3][1] < 70 or students[4][1] < 70 or students[5][1] < 70 or students[6][1] < 70:
    i.append(students[6])
    print(f"Stutdent needing improvement : {students[3][0]}, {students[5][0]}")


if i[4] >= 80:
    print(f"High performers = {students[0][0]}: {students[0][4]:.2f}, {students[1][0]}: {students[1][4]:.2f}, {students[2][0]}: {students[2][4]:.2f}, {students[4][0]}: {students[4][4]:.2f}, {students[6][0]}: {students[6][4]:.2f}") 


top_students = max(students, key=lambda x: x[4])
print(f"Top Student : {top_students[0]}: {top_students[4]:.2f}")


math_avg = sum(students[i][1] for i in range(len(students))) / len(students)
print(f"Math avg : {math_avg:.2f}") 


sci_avg = sum(students[i][2] for i in range(len(students))) / len(students)
print(f"Science avg : {sci_avg:.2f}")


eng_avg = sum(students[i][3] for i in range(len(students))) / len(students)
print(f"English avg : {eng_avg:.2f}")    