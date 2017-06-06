class Trie(object):
    def __init__(self, data=None):
        self.data = data
        self.children = []
        self.end = False

    def insert(self, word):
        if word == '':
            self.end = True
            return None
        #write base case
        char = word[0]
        found = False
        for child in self.children:
            if child.data == char:
                found = True
                trie_node = child
                break
        if not found:
            trie_node = Trie(data=char)
            self.children.append(trie_node)
        trie_node.insert(word[1:])

    def look_up(self, word):
        curr = self.travel(word)
        if curr is None:
            return False
        else:
            return curr.end

    def travel(self, word):
        if word == '':
            return self
        char = word[0]
        found = False
        for child in self.children:
            if child.data == char:
                found = True
                trie_node = child
                break
        if not found:
            return None
        else:
            return trie_node.travel(word[1:])

    def is_concat_2_words(self, word):
        main_trie = self
        if word == '':
            return False
        curr = self
        for i in range(len(word)):
            char = word[i]
            curr = curr.travel(char)
            if curr is None:
                return False
            else: #curr not None
                if curr.end:
                    if main_trie.look_up(word[i+1:]):
                        return True
                    else:
                        continue
                else: # curr is not end
                    continue


def main():
    t1 = Trie()
    t2 = Trie()
    t3 = Trie()
    words1 = ['news', 'abcd', 'tree', 'geeks', 'paper']
    words2 = ['geeks', 'code', 'xyz', 'forgeeks', 'paper']
    words3 = ['geek', 'code', 'xyz', 'forgeeks', 'paper']
    [t1.insert(w) for w in words1]
    [t2.insert(w) for w in words2]
    [t3.insert(w) for w in words3]
    print t1.is_concat_2_words('newspaper') # True
    print t2.is_concat_2_words('geeksforgeeks') # True
    print t3.is_concat_2_words('geeksforgeeks') # False

if __name__ == '__main__':
    main()
