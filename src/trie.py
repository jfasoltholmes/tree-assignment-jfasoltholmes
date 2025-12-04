from trie_interface import ITrie
from typing import Optional

class TrieNode: 
    def __init__(self) -> None:
        self.children = {}
        self.isEndOfWord = False
        self.info = {}

class Trie(ITrie):
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, name: str, info: dict) -> None:
        cur = self.root

        # Standardizing name to lowercase
        for c in name.lower():
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEndOfWord = True

        # Storing original name with info for displaying
        info["name"] = name
        cur.info = info

    def remove(self, name: str) -> bool:
        if not name:
            return False
        
        status = {"deleted": False}
        
        def _remove(cur: TrieNode, index: int) -> bool:
            # Reached end of the name
            if index == len(name):
                if not cur.isEndOfWord:
                    return False  # Name not found
                cur.isEndOfWord = False
                cur.info = {}
                status["deleted"] = True
                return len(cur.children) == 0  # If there is no children, node can be deleted
            
            c = name[index].lower()
            if c not in cur.children:
                return False  # Name not found
            
            childNode = cur.children[c]
            shouldDeleteChild = _remove(childNode, index + 1)

            if shouldDeleteChild:
                del cur.children[c]
                return len(cur.children) == 0 and not cur.isEndOfWord
            return False
        
        _remove(self.root, 0)
    
        # Return whether deletion was successful
        return status["deleted"]

    def search(self, name: str) -> Optional[dict]:
        cur = self.root

        for c in name.lower():
            if c not in cur.children:
                return None
            cur = cur.children[c]
        
        if cur.isEndOfWord:
            return cur.info
        return None

    def autocomplete(self, prefix: str) -> list[tuple[str, dict]]:
        results = []
        cur = self.root

        for c in prefix.lower():
            if c not in cur.children:
                return results  # No names with this prefix
            cur = cur.children[c]

        def _dfs(node: TrieNode):
            if node.isEndOfWord:
                results.append((node.info["name"], node.info))

            for char in node.children:
                _dfs(node.children[char])
            
        _dfs(cur)
        return results