points = int(input("Number of received points (0-100): "))

if points < 0 or points > 100:
    print("Error. Invalid data.")
elif points <= 49:
    print("Незадовільно")
elif points <= 69:
    print("Задовільно")
elif points <= 89:
    print("Добре")
else:
    print("Відмінно")