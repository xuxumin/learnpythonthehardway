# excerise 6: Strings and Text
types_of_people = 10
# string inside string x
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# two strings inside string y
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
# string hilarious inside string joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
