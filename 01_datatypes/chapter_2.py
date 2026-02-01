# Demonstrating the mutability of Set in Python

spice_mix = set()
print(f"Inital spice mix id: {id(spice_mix)}")
print(f"Initial spice mix: {spice_mix}")
spice_mix.add("Ginger")
spice_mix.add("Cinnamon")
spice_mix.add("Cardamom")
print(f"After spicemix id: {id(spice_mix)}")
print(f"After spicemix: {spice_mix}")