students = {}
while True:
    name = input("Enter student's name (done): ").capitalize()
    if name == "Done":
        break
    else:
        grade = int(input(f"Enter {name}'s grade: "))
        students[name] = {"Grade" : grade}

total = 0
for i, j in students.items():
    if j["Grade"] >= 90:
        print(f"{i} has an A. Excellent work!")
    elif j["Grade"] >= 80:
        print(f"{i} has an B. Good job!")
    elif j["Grade"] >= 70:
        print(f"{i} has an C. Good!")
    elif j["Grade"] >= 60:
        print(f"{i} has an D. Not bad!")
    elif j["Grade"] >= 50:
        print(f"{i} has failed. Additional support needed.")
    total += j["Grade"]
    
print(f"Class average: {float(total // len(students))}")
