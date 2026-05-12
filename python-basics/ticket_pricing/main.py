age = int(input("Enter your age: "))

if age>=60:
    ticket=8
elif age<12:
    ticket=5
else:
    ticket=10

print(f"Ticket Price: ${ticket}")
