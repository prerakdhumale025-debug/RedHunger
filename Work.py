def print_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Taking user input
number = int(input("Enter a number: "))
print_table(number)


#Re-Write table function using while looop
def table_new(num):
    number = int(input("Enter a number: "))
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1
table_new()