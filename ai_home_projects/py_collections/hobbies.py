my_hobbies = {"Reading", "Traveling", "Cooking", "Hiking", "Photography"}
friends_hobbies = {"Gaming", "Cooking", "Traveling", "Music", "Sports"}

# Find common hobbies
common_hobbies = my_hobbies.intersection(friends_hobbies)
print(f"Common hobbies:\n {common_hobbies}\n")

# Find unique hobbies
unique_hobbies = my_hobbies.difference(friends_hobbies)
print(f"Unique hobbies:\n {unique_hobbies}")

