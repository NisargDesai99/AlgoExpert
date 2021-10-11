
def closest_value_bst(tree, target):



def create_bst(bst_values):
    bst = BST()
    for value in bst_values:
        bst.add(value)



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if self.value == None:


    def __add(self, value):
        if self.value == None:

            return
        elif self.value <= value:
            self.right = value
            return
        elif self.value > value:
            self.left = value
            return

    def __repr__(self):

