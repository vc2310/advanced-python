# unpacking
# first, second = (1, 2)

# print(first)
# print(second)


# first, second, *remaining = (1, 2, 3, 4, 5)

# print(first)
# print(second)
# print(remaining)

fruits = ["apple", "orange", "plum", "avocados"]
vegetables = ["jicama", "asparagus", "okra", "potato"]


# fruits_and_vegetables = [*fruits, *vegetables, "arugula"]
# print(fruits_and_vegetables)

# fruits_and_vegetables2 = fruits + vegetables + ["arugula"]
# print(fruits_and_vegetables2)


print([*fruits, *fruits])
print(fruits + fruits)
print(fruits * 2) # Eric would not do it this way


# person = {"fn": "Bob", "ln": "Smith"}

# person_private_data = {
#     "ssn": "123-45-6789",
#     "dl": "2T4-56-H126",
# }

# total_person = {**person, **person_private_data}

# print(total_person)
