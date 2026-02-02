import sys
from fractions import Fraction
from decimal import Decimal as D

ideal_temp = 92.5 #Fahrenhiet
current_temp = 91.49
print(f"Ideal temp {ideal_temp}")
print(f"Current temp {current_temp}")
print(f"Difference in temp { ideal_temp - current_temp }")

# Checking System Float Representation with using module (sys)
print(f"{sys.float_info}")