# Interface for Trie data structure
from __future__ import annotations
from typing import Protocol, Optional

class ITrie(Protocol):
    def insert(self, name: str, info: dict) -> None: 
        """Inserts a contact name with contact info into the trie.
        Time: O(n) where n is the length of the name.
        Space: O(n) for storing the name and info.
        """
    def remove(self, name: str) -> bool: 
        """Removes a contact name from the trie.
        Time: O(n) where n is the length of the name.
        Space: O(n) for the recursion stack.
        """
    def search(self, name: str) -> Optional[dict]: 
        """Searches for a contact name and returns the contact info. Return None if not found.
        Time: O(n) where n is the length of the name. 
        Space: O(1)
        """
    def autocomplete(self, prefix: str) -> list[tuple[str, dict]]: 
        """Returns a list of contact names and their contact info that start with the given prefix.
        Time: O(p + c) where p is the length of the prefix and c is the number of contacts with the prefix.
        Space: O(c + h) where h is the height of the tree.
        """