items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]
print("Numbered Shopping List:")
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")

print()

count_more_than_4 = 0
for item in items:
    if len(item) > 4:
        count_more_than_4 += 1

print(f"Items with more than 4 letters: {count_more_than_4}")
print()

longest_item = items[0]
for item in items:
    if len(item) > len(longest_item):
        longest_item = item

print(f"Longest item name: {longest_item}")