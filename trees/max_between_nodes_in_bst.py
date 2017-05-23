class BST(object):
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.data is None:
            self.data = val
        else:
            if val > self.data:
                if self.right is None:
                    self.right = BST(val)
                else:
                    self.right.insert(val)
            elif val < self.data:
                if self.left is None:
                    self.left = BST(val)
                else:
                    self.left.insert(val)

    @staticmethod
    def create_bst(input_list):
        bst = None
        for data in input_list:
            n = BST(data)
            if bst is None:
                bst = n
            else:
                bst.insert(data)
        return bst

    def find_lca_including_self(self, n1, n2):
        if n1 == self.data or n2 == self.data:
            return self
        elif (n1 > self.data and n2 < self.data) or (n1 < self.data and n2 > self.data):
            return self
        elif n1 > self.data and n2 > self.data:
            if self.right is None:
                raise Exception("The numbers are not even present in the BST")
            return self.right.find_lca_including_self(n1, n2)
        elif n1 < self.data and n2 < self.data:
            if self.left is None:
                raise Exception("The numbers are not even present in the BST")
            return self.left.find_lca_including_self(n1, n2)

    def max_between_nodes(self, n1, n2):
        lca = self.find_lca_including_self(n1, n2)
        curr_node = lca
        s = max(n1, n2)

        while curr_node is not None:
            if curr_node.data == s:
                return curr_node
            elif curr_node.data > s:
                return curr_node
            else:
                curr_node = curr_node.right
        return curr_node
