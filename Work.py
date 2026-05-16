def print_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Taking user input
number = int(input("Enter a number: "))

# Calling function
print_table(number)
