import random
lottery_tickets = []
print("Creating 100 random tickets")
for i in range(100):
    lottery_tickets.append(random.randrange(1, 99))
winners = random.sample(lottery_tickets, 2)
print(f"Lucky 2 lottery tickets are {winners}")