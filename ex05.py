name = 'Xumin Xu'
age = 24 # not a lie
height = 183 # cm
weight = 77 # kg
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print("He's {} cm tall. (or {} inches)".format(height, round(height/2.54, 2)))
print("He's {} kg heavy. (or {} lbs)".format(weight, round(weight * 2.2, 2)))
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
