def char_to_int(char):
    return ord(char) - ord('a')

class Trie(object):
    def __init__(self, data=None):
        self.data = data
        self.children = []
        self.end = False

    def insert(self, word):
        if word == '':
            self.end=True
            return
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

    def print_valid_words(self, arr_hash, prefix=''):
        res = []
        if self.end and prefix  !='':
            res.append(prefix)
        for child in self.children:
            index = char_to_int(child.data)
            if arr_hash[index]:
                res.extend(child.print_valid_words(arr_hash, prefix + child.data))
        return res

def main():
    arr = {'e', 'o', 'b', 'a', 'm', 'g', 'l'}
    arr_hash = [False]*26
    for c in arr:
        index = char_to_int(c)
        arr_hash[index] = True
    words = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
    t = Trie()
    for word in words:
        t.insert(word)
    print t.print_valid_words(arr_hash)

if __name__ == '__main__':
    main()
