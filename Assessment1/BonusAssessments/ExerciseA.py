# Define the range of tables
for num in range(1, 11):
    print(f"Multiplication table of : {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print()
