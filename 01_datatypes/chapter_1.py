# Demonstrating immutability of integers in Python

initial_sugar_amount = 2
print(f"Initial sugar amount: {initial_sugar_amount}")
print(f"Initial sugar ID: {id(initial_sugar_amount)}")

updated_sugar_amount = 12
print(f"Updated sugar amount: {updated_sugar_amount}")
print(f"Updated sugar ID: {id(updated_sugar_amount)}")
