def LISS(root):
    print('LISS: root:', root)
    
from collections import defaultdict

class Node:
    def __init__(self, val, parent) -> None:
        self.data = val
        self.left = None
        self.right = None
        self.parent = parent


class Tree:
    def __init__(self) -> None:
        self.root = None
        self.map_nodes = defaultdict(Node)
    
    def Insert(self, parent, child, dir):
        if self.root is None:
            root_node = Node(parent, None)
            child_node = Node(child, root_node)
            if dir == 'L':
                root_node.left = child_node
            else:
                root_node.right = child_node
            self.root = root_node
            self.map_nodes[parent] = root_node
            self.map_nodes[child] = child_node
            return
        parent_node = self.map_nodes[parent]
        child_node = Node(child, parent_node)
        self.map_nodes[child] = child_node
        if dir == 'L':
            parent_node.left = child_node
        else:
            parent_node.right = child_node
        return

if __name__ == "__main__":
    # test_cases = int(input())
    test_cases = 1
    for cases in range(test_cases):
        # n = int(input())
        n = 4
        # a = list(map(str, input().strip().split()))
        a = list(map(str, "10 20 L 10 30 R 20 40 L 20 60 R".strip().split()))

        tree = Tree()
        i = 0
        while (i < len(a)):
            parent = int(a[i])
            child = int(a[i + 1])
            dir = a[i + 2]
            i += 3
            tree.Insert(parent, child, dir)

        print(LISS(tree.root))
