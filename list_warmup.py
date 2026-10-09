# 1.Create a list called fruits
fruits = ["apple", "banana", "orange", "mango"]

# 2.Print the first and the last item using indexes.
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# 3. append() a fifth fruit,then print the whole list.
fruits.append("pineapple")
print(f"After appending: {fruits}")

# 4. remove() one fruit, then print the list again.
fruits.remove("banana")
print(f"After removing: {fruits}")

# 5. Print how many fruits remain using len().
print(f"Number of fruits remaining: {len(fruits)}")
