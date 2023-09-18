# Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

# Program:-

import json

state_capitals = {}

for i in range(7):
    state = input(f"Enter the name of Indian State {i + 1}: \n")
    capital = input(f"Enter the capital of {state}: \n")
    state_capitals[state] = capital

with open("Indian_States.json", "w") as file:
    json.dump(state_capitals, file, indent=4)

print("State-Capital Information saved to  'Indian_States.json'")