class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

def create_tree_from_list(list):
    if len(list) == 0:
        return None
        
    root = Node(list[0])

    for child in list[1:]:
        root.children.append(Node(child))
        return root

input_list = [1,2,3,4]
root = create_tree_from_list(input_list)
