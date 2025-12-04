# Jordan Fasolt-Holmes
# Project Title and Description
The tree I implemented was a Trie. I chose a trie because, by design, it makes autocomplete much easier. My application is a simple interface that allows a user to add, delete, and search for contacts. When searching, the application uses a trie to show auto complete suggestions for contact names. Typically, those that will benefit the most from this tool are people that need a lightweight, autocomplete tool for managing large lists of people or contact info.

# Installation and Setup
To install and run, in the home directory of the application, run the following 2 lines:

pip install -r requirements.txt

python src/application.py

# Usage Guide
The application will begin by providing 10 sample contacts, from there you can navigate by scrolling the contact list or by searching using the search bar in the upper left corner, this will provide you with an auto complete of the name you are trying to search. You can also add a contact by clicking the button in the top left corner, or delete a contact by clicking the view button on a contact and clicking the delete button at the bottom of the contact details page.

# Screenshots
![Demo Screenshot 1](https://github.com/jfasoltholmes/tree-assignment-jfasoltholmes/blob/main/screenshots/trie_ss1.png?raw=true)

![Demo Screenshot 2](https://github.com/jfasoltholmes/tree-assignment-jfasoltholmes/blob/main/screenshots/tree_ss2.png?raw=true)

![Demo Screenshot 3](https://github.com/jfasoltholmes/tree-assignment-jfasoltholmes/blob/main/screenshots/trie_ss3.png?raw=true)
# Tree Implementation Details
The tree that was implemented is the Trie structure. The structure works by storing each letter of a string as a node in a tree, then end of a name is marked at the last node of a name. This allows for easy name searching along with auto complete by prefixes. The key operations are insert, search, remove, and autocomplete. 

Insert: 
- Time Complexity: O(n) where n is the length of the name.
- Space Complexity: O(n) for storing the name and info.

Search: 
- Time Complexity: O(n) where n is the length of the name. 
- Space Complexity: O(1)

Remove: 
- Time Complexity: O(n) where n is the length of the name.
- Space Complexity: O(n) for the recursion stack.

Autocomplete: 
- Time Complexity: O(p + c) where p is the length of the prefix and c is the number of contacts with the prefix.
- Space Complexity: O(c + h) where h is the height of the tree.

# Evolution of the Interface
Initially, my return type for remove caused GUI bugs. I originally had my remove method set to return None. As a result, the GUI was unable update when removing a contact. To fix this, I changed the return type to boolean allowing remove to return wether it successfully deleted the contact or not. This had also helepd to seperate the success of deleting the comtact and the success of pruning nodes. This fixed all GUI updates. I had also changed the return type of search from a dict to an Optional dict. This felt safer than returning an empty dictionary even if there where no found contacts. I learned that no matter what iteration is apart of the process is software design. It helps to write everything out to plan but iteration will always be an important step.

# Challenges & Solutions
A big challenege for my was designing the GUI in a user friendly way, especially doing so outside of my usual tools. At first I had attempted to create the GUI in one application class. This had become incredibly difficult to maintain which lead me to the idea of breaking the GUI into multiple classes for the different pages/windows. This made for more readable code and as a result the overall process better.

# Future Enhancements
I think that allowing users to add contact photos would make for an interesting challenege to implement. It could also be interesting to convert this into a web application with authentication and a database for multiple users to store their own contacts.
