def greet (name):
    print(f"Hello, {name}!")

greet("Brady")
greet("Hillary")

def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(5, 3)
print(f"The total is: {total}")

def calculate_apple_cost(num_apples, price_each):
    return num_apples * price_each

cost = calculate_apple_cost(5, 0.50)
print(f"5 apples cost ${cost}")