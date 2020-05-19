import string



class Trie:

    # NOTE:
    # Implement a Node's child list with a list or dict?
    # - dict takes up more space but is more flexible
    # - BSTs vs Tries: Aside from the obvious different in structure, a trie
    #   is different from a BST in that the set of all possible values for
    #   a node can be stored at the node beforehand, but there's this idea of
    #   the value being turned on/off at the node. If a certain char is not
    #   associated with a node, then it is turned off (e.g., its child is
    #   None) for that node. Else, that char is turned on for that node.
    # - If using a list, the indices of the list can somehow represent
    #   the character associated with the TrieNode at that index.

    def __init__(self):
        self.num_nodes = 0
        self.root = TrieNode()


    def insert(self, s):
        #s = [c for c in s]
        # Use s.pop(0) to insert each char into Trie? Nah, try for loop...

        # Should first search if string exists in Trie before inserting???
        # - But the procedure for searching is pretty similar to inserting.
        #   Why not just go with the insertion procedure anyway?
        #if not self._search(s):
        cur_node = self.root
        for i in range(len(s)):
            if not cur_node.children[s[i]]:
                cur_node.children[s[i]] = TrieNode()

            cur_node = cur_node.children[s[i]]

        cur_node.is_end_of_word = True


    def search(self, s):
        # Cases:
        # - You go all the way to the end of s and its not a string
        #   in the trie. (e.g., you search for "dude" and the Trie
        #   contains "dudes"...?)
        # - At any point during the processing of s (but not the end
        #   of s), you find a char that is not in the Trie
        cur_node = self.root
        for i in range(len(s)):
            if not cur_node.children[s[i]]:
                return False
            cur_node = cur_node.children[s[i]]
            # ^IMPORTANT. "Increments" cur_node.

        return True if cur_node.is_end_of_word else False


    def auto_complete(self, s, peek_len):
        # THINK:
        # - Consider the notion of "peeking" ahead of the string (s)
        #   provided by the user (extent of peeking indicated by peek_len)
        #   to get the set of candidate strings.
        pass



class TrieNode:

    # NOTE:
    # . A node has a data structure for storing its children. The size
    #   of the data structure should be the size of whatever alphabet
    #   you're using.
    #   - Can have that data structure be a list that stores other TrieNodes.
    #     The indices of the list can represent the char associated with the
    #     TrieNode. These TrieNodes represent the child char associated with
    #     the char represented by the index.
    #   - Can use a dict where keys are chars and values are TrieNodes
    #     that represent
    # . Have an instance variable is_end_of_word

    def __init__(self):
        # Scratch thoughts:
        # . A node should only have a single child for each letter???
        #   - Perhaps the visual representaiton of a Trie doesn't really
        #     align with its implementation??? It's easier to visualize levels
        #     as opposed to an actual tree??? ... Or perhaps it's a matter of
        #     a position in the dict being filled/unfilled...
        #   - A node's char value is determined by what its parent says??? Or
        #     perhaps think this: a key is the current node's chars and values
        #     are the child nodes associated with those individual chars...yeah!
        #     This sounds about right.
        self.children = { l:None for l in
                           string.ascii_lowercase +
                           string.ascii_uppercase }
        self.is_end_of_word = False



if __name__ == "__main__":
    trie = Trie()
    trie.insert("dudes")
    print(trie.search("dudes"))
    print(trie.search("dude"))
