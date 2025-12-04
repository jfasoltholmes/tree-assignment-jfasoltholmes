# Tree Selection: Which tree did you choose and why?
- I chose the trie structure for my application because it allows for the most efficient autcomplete.
# Use Cases: What problems does this tree solve well?
- The trie is perfect in the context of a phonebook application because it allows for very quick searching, deletions, and organization for autocompleting names.
# Properties: What makes this tree unique? What are its performance characteristics?
- The trie is particularily unique because unlike other tries it stores words by breaking up each letter to be a node in the tree structure. The full word is represented by the path from the root to a node that is marked as the end of a word.
# Interface Design: Method signatures with descriptions
 - What operations does your tree support
 1. Insert
 2. Search
 3. Remove
 4. Autocomplete
 - What are the parameters and return types?
 Insert takes the name and contact data, it returns None
 Search takes the name of the contact and optionall returns a dictionary or None
 Remove takes the name of the contact and returns a boolean
 Autocomplete takes the prefix and returns a List[tuple[str, dict]]
 - What is the Big-O time complexity of each operation? (Required for every method)
 Insert: O(n) where n is the length of the name
 Search: O(n) where n is the length of the name
 Remove: O(n) where n is the length of the name
 Autocomplete: O(p + c) where p is the length of the prefix and c is the number of contacts with the prefix
 - What is the space complexity? (if relevant)
 Insert: O(n) 
 Search: O(1) 
 Remove: O(n) 
 Autocomplete: O(c + h) where c is the number of contacts with the prefix and h is the height of the tree.

# Implementation Notes: Key algorithms or techniques you'll use
- Depth First Search for autocomplete