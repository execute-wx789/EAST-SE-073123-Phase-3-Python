# Sequence Types

# Creating Lists
#✅ 1. Create a list of 10 pet names
pet_names = ["Momo", "Ejay", "Ari", "Marcline", "Abby", "Ellie", "Sarah", "Mollie", "Polar"]
#------------------------ Reading Information from Lists
#✅ 2. Return the first pet name 

# print(pet_names[0])

#✅ 3. Return the last value

# print(pet_names[-1])

#✅ 4. Return all pet names beginning from the 3rd index

# print(pet_names[3:])

#✅ 5. Return all pet names before the 3rd index

# print(pet_names[:3])

#✅ 6.  Return all pet names beginning from the 3rd index and up to (exclusive of) the 7th

# print(pet_names[3:7])

#✅ 7. Find the index of a given element

# print(pet_names.index("Abby"))

#✅ 8. Reverse the original list

# print(pet_names[::-1])


# print(pet_names.reverse())

#✅ 9. Return the frequency of a given element 

# print(pet_names.count("Abby"))

#---------------------------------- Updating Lists
#✅ 10. Change the first element to all uppercase

# pet_names[0] = pet_names[0].upper()
# pet_names[pet_names.index("Abby")] = pet_names[pet_names.index("Abby")].upper()
# print(pet_names)

#---------------------------------- Adding items to list
#✅ 11. Append a new name to the list

# pet_names.append("Blu")
# print(pet_names)

#✅ 12. Add a new name at a specific index

# pet_names.insert(1, "Coco")
# print(pet_names)

#✅ 13. Add two lists together 

# added_list = [1,2,3] + [4,5,6]
# print(added_list)

#---------------------------------- Removing 
#✅ 14. Remove the final element from the list

# pet_names.pop()
# print(pet_names)

#✅ 15. Remove element by specific index

# pet_names.pop(3)
# print(pet_names)

#✅ 16. Remove a specific element 

# print(pet_names)
# pet_names.remove("Sarah")
# print(pet_names)

#✅ 17. Remove all pet names from the list

# pet_names.clear()
# print(pet_names)

#---------------------------------- Tuple 
#✅ 18. Create a Tuple of pet 10 ages 

pet_ages = (3,2,6,1,6,7,2,5)

#✅ 19. Print the first pet age

# print(pet_ages[0])

#---------------------------------- Testing Changeability 
#✅ 20. Attempt to remove an element with .pop (should error)

# pet_ages.pop()

#✅ 21. Attempt to change the first element (should error)

# pet_ages[0] = "sdkfj"

#---------------------------------- Tuple Methods
#✅ 21. Return the frequency of a given element

# pet_ages.count(6)

#✅ 22. Return the index of first matching element 

# pet_ages.index(2)

#✅ 23. Create a range 

# range_1 = range(0,10,2)
# for i in range_1:
#     print(i)

#---------------------------------- Demo Sets (stretch goal)
#✅ 24. Create a set of 3 pet foods

# Demo Dictionaries 
#---------------------------------- Creating 
#✅ 25.  Create a dictionary of pet information with the keys name, age and breed

momo = {"name": "momo","weight":"fat","hobby":"waiting for food","cuddliness":2, "age":3}

#✅ 26.  Use dict to create a dictionary of pet information with the keys name, age and breed

momo_dict = dict()

#---------------------------------- Reading
#✅ 27. Print the pet attribute of name using bracket notation

# print(momo["cuddliness"])

#✅ 28. Print the pet attribute of age using .get

# print(momo.get("name"))

#---------------------------------- Updating 
#✅ 29. Update the pets age to 12

# momo["age"] = 12
# print(momo)

#✅ 30. Update the other pets age to 26

#---------------------------------- Deleting
#✅ 30. Delete a pets age using the del keyword 

# del momo["hobby"]
# print(momo)

#✅ 31. Delete the other pets age using the .pop, returns removed value

# momo.pop("age")
# print(momo)

#✅ 32. Delete the last item in the pet dictionary using popitem()

# momo.popitem()
# print(momo)

#---------------------------------- Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
]
#✅ 33. loop through a range of 10 and print every number within the range

# for i in range(1,10):
#     print(i)

#✅ 34. loop through a range between 50 and 60 that iterates by 2 and print every number

# for i in range(50,60,2):
#     print(i)

#✅ 35. Loop through the pet_info list and print every dictionary  

# for pet in pet_info:
#     print(pet.get("breed"))

#✅ 36. Create a function that takes a list as an argument. 
    # The function should use a for loop to loop through the list and print every item in the list 
    # Invoke the function and pass it pet_names as an argument

# def print_info(lst=pet_info)
#     for pet in pet_info:
#         print(pet)

#✅ 37. Create a function that takes a list as an argument.(simple example) 
    # The function should define a counter and set it to 0
    # Create a while loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # return the counter 

# def count(info=pet_info):
#     counter = 0
#     while(counter < len(info)):
#         counter += 1
#     return counter
# print(count(pet_info))

#✅ 38. Create a function that updates the age of a given pet
        # The function should take a list of dicts, name and age as parameters 
        # Create a index variable and set it to 0
        # Create a while loop. 
            # The loop will continue so long as the list does not contain a name matching the name param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found update the items age with the new age 
        # else return 'pet not found'

# def update_age(name, age, info=pet_info):
#     cur_index = 0
#     while(cur_index < len(info) and info[cur_index].get("name") != name):
#         cur_index += 1
#     if(cur_index == len(info)):
#         print("error")
#     else:
#         info[cur_index]["age"] = age

# update_age("test",0)
# print(pet_info)

#✅ 39. Use list comprehension to return a list containing every pet name from pet_info changed to uppercase

# pet_names_upper = [pet.get("name").upper() for pet in pet_info]
# print(pet_names_upper)

#✅ 40. Use list comprehension to find a pet named spot

# find_pet = [pet for pet in pet_info if pet.get("name") == "spot"]
# print(find_pet)

#✅ 41. Use list comprehension to find all of the pets under 3 years old

# find_young_pets = [pet for pet in pet_info if pet.get("age") < 3]
# print(find_young_pets)

#✅ 43. Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 
