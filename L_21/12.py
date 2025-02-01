import random
students = ["Maksat", "Yhlas", "Nurly", "Resul", "Baymyrat"]
print(random.choice(students))
print(random.sample(students, 2))
random.shuffle(students)
print(students)