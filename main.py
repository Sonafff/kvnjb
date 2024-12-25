a = int(input("1-st number: "))
b = int(input("2-nd number: : "))
ab = input("Action(/, *, -, +): ")

if ab == '+':
    print(f"Result: {a + b}")
elif ab == '-':
    print(f"Result: {a - b}")
elif ab == '*':
    print(f"Result: {a * b}")
elif ab == '/':
    if b == 0:
        print("invalid data(division by 0).")
    else:
        print(f"Result: {a / b}")
else:
    print("unknown operation.")