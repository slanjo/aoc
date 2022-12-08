from collections import defaultdict 
#with open("input.txt", "r") as data:
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


if __name__ == '__main__':
    SZ = defaultdict(int) 
    path = []
    with open("input_t.txt", "r") as feed:
            data = feed.read().strip()
            lines = [x for x in data.split('\n')]
            #X.append(l.strip().split())

    input_list =  lines
    root = create_tree_from_list(input_list)
    print(root.__dict__) 
