is_milk_boiling = True
stir_count = 5
total_actions = is_milk_boiling + stir_count
print(f"Total Actions: {total_actions}")

milk_present = 1 # this can be either like 1,TRUE, OR False,0,None. for right now we've assume that the milk is available.
print(f"is there milk {bool(milk_present)}")

# Example WITH (AND) Boolean Operator

is_water_hot = True
tea_added = False
can_serve_tea = is_water_hot and tea_added
print(f"can we serve chai? {can_serve_tea}")