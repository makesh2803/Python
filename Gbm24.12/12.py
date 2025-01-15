num_of_students = 0
passed_students = 0
overall_percent = 100
while True:
    score = int(input("Enter student score: "))
    if score == 0:
        break
    else:
        num_of_students += 1
        passed_students += score >= 50 
print(f"{int((overall_percent * passed_students) / num_of_students)} percent of student passed the exam")