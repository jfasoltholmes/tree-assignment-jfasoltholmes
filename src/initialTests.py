from trie import Trie
#from customtkinter import CTk, CTkLabel, CTkButton

phonebook = Trie()
# test inserts
phonebook.insert("Alice", {"phone": "123-456-7890", "email": "alice@example.com"})
phonebook.insert("Bob", {"phone": "987-654-3210", "email": "bob@example.com"})
phonebook.insert("Alina", {"phone": "555-555-5555", "email": "alina@example.com"})
phonebook.insert("Albert", {"phone": "111-222-3333", "email": "albert@example.com"})

# test search
result = phonebook.search("Alice")
if result:
    print(f"[PASS]Found Alice: {result}")
else:
    print("Alice not found")

unknown = phonebook.search("Charlie")
if unknown is None:
    print("[PASS]Charlie not found")
else:
    print("Charlie found unexpectedly")

# test autocomplete
results = phonebook.autocomplete("Al")
names = [r[0] for r in results]
print(f"Autocomplete for 'Al': {names}")
if "Alice" in names and "Alina" in names and "Albert" in names:
    print("[PASS]Autocomplete returned correct names")
else:
    print("Autocomplete missing expected names")

# test remove
print("Removing Alice...")
phonebook.remove("Alice")

if phonebook.search("Alice") is None:
    print("[PASS]Alice successfully removed")
else:
    print("Failed to remove Alice")

if phonebook.search("Alina") is not None:
    print("[PASS]Alina still present after removing Alice")
else:
    print("Alina missing after removing Alice")
