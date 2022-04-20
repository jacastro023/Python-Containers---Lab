# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.
print("exercise 1: ")
students = ['Jose', 'lilly', 'Danny', 'Diana', 'Stephanie']
print(students[1])
print(students[-1])


# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "food goes here is a good food".
print("exercise 2: ")
foods = ('apple pie', 'hotdog', 'sandwhich', 'steak', 'chicken')
for food in foods:
    print(f"{food} is a good food")


# Exercise 3
# Using a for loop, print just the last two food strings from foods.
print("exercise 3: ")
for food in foods[-2:]:
    print(food)


# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"
print("exercise 4: ")
home_town = {
    'city': 'chicago',
    'state': 'Illinois',
    'population': '2.75M'
}

print(f"I was born in {home_town['city']}, {home_town['state']} - {home_town['population']} of population")


# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"
print("exercise 5: ")
for key, val in home_town.items():
    print(f"{key} = {val}")


# Exercise 6
# Create an empty list named cohort.
print("exercise 6: ")
cohort = []
# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:
for index, student in enumerate(students):
  cohort.append({
    'student': student,
    'fav_food': foods[index]
  })


#  {
#    'student': 'Tina',
#    'fav_food' 'Cheeseburger'
#  }
# Iterate over cohort printing out each element.
for student in cohort:
  print(student)


# Exercise 7
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.
print("exercise 7: ")
awesome_students = [f"{s} is awesome!" for s in students]
for s in awesome_students:
    print(s)



# Exercise 8
# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.
print("exercise 8: ")
for f in [food for food in foods if 'a' in food]:
    print(f)