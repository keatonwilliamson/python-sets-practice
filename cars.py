# 1. Create an empty set named showroom.
# 2. Add four of your favorite car model names to the set.
showroom = {"Toyota", "Nissan", "Ford", "Honda"}

# 3. Print the length of your set.
print(len(showroom))

# 4. Pick one of the items in your show room and add it to the set again.
showroom.add("Toyota")
print(len(showroom))

# 5. Using update(), add two more car models to your showroom with another set.
showroom.update({"Cadillac", "Chevy"})
print(len(showroom))

# 6. You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("Cadillac")
print(len(showroom))

# Acquiring more cars
# 1. Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = {"Toyota", "Subaru", "Mazda", "Ford"}

# 2. Use the intersection method to see which cars exist in both the showroom and that junkyard.
intersectingCars = showroom.intersection(junkyard)
print(intersectingCars)

# 3. Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
showroom = showroom.union(junkyard)
print(showroom)

# 4. Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.
showroom.discard("Subaru")
print(showroom)







