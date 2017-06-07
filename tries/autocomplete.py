# get all the words with the given prefix

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
        found = False
        for child in self.children:
            if child.data == char:
                found = True
                trie_node = child
                break
        if not found:
            trie_node = Trie(data=char)
            self.children.append(trie_node)
        return trie_node.insert(word[1:])

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

    def get_words(self, prefix=''):
        res = []
        if self.end:
            res.append(prefix)
        for child in self.children:
            res.extend(child.get_words(prefix + child.data))
        return res

    def get_words_with_prefix(self, prefix):
        curr = self.travel(prefix)
        if curr is None:
            return -1
        else:
            return curr.get_words(prefix)

def main():
    words = ['abc', 'abcd', 'aa', 'abbbaba']
    prefix = 'ab'
    t = Trie()
    [t.insert(word) for word in words]
    print t.get_words_with_prefix(prefix)

if __name__ == '__main__':
    main()
