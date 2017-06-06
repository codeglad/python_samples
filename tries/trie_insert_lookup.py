
class Trie(object):
    def __init__(self, data=None):
        self.data = data
        self.children = []
        self.end = False

    def insert(self, word):
        if word == '':
            self.end = True
            return None
        char = word[0]
        is_char_present = False
        for child in self.children:
            if child.data == char:
                is_char_present = True
                trie_node = child
                break
        if not is_char_present:
            trie_node = Trie(data=char)
            self.children.append(trie_node)
        trie_node.insert(word[1:])

    def look_up(self, word):
        if word == '':
            return self.end
        char = word[0]
        found = False
        for child in self.children:
            if child.data == char:
                found = True
                trie_node = child
                break
        if not found:
            return False
        else:
            return trie_node.look_up(word[1:])


def main():
    t = Trie()
    words = ['news', 'abcd', 'tree', 'geeks', 'paper']
    [t.insert(word) for word in words]
    print t.look_up('tree') # True
    print t.look_up('pape') # False

if __name__ == '__main__':
    main()
