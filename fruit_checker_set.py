fridge = {"banana", "apple", "kiwi", "orange", "grapes"}
eaten_input = input("🍽️ Enter the fruits you ate (comma-separated): ").lower()

eaten = set(f.strip() for f in eaten_input.split(","))
common = fridge.intersection(eaten)
not_in_fridge = eaten.difference(fridge)
left = fridge.difference(eaten)

print("😋 You ate these from your fridge:", common)
print("🤔 These fruits were NOT in your fridge:", not_in_fridge)
print("🍏 Fruits left in the fridge:", left)


Enter the fruits you ate (comma-separated): banana, kiwi, cherry
