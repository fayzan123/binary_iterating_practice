import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def generate_random_tree(size):
    if size == 0:
        return None
    left_size = random.randint(0, size-1)
    right_size = size - 1 - left_size

    left_subtree = generate_random_tree(left_size)
    right_subtree = generate_random_tree(right_size)
    root = Node(random.randint(0, 100))
    root.left = left_subtree
    root.right = right_subtree
    return root
def tree_height(root):
    if root is None:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))

def fill_positions(root, depth, pos, positions, shift):
    if root is None:
        return
    positions.append((depth, pos, root.value))
    fill_positions(root.left, depth + 1, pos - shift // 2, positions, shift // 2)
    fill_positions(root.right, depth + 1, pos + shift // 2, positions, shift // 2)

def print_tree_2d(root):
    height = tree_height(root)
    width = (2 ** height) * 2  # Width based on tree height

    # Initialize 2D grid
    grid = [[" " for _ in range(width)] for _ in range(height * 2)]

    # Get positions of each node
    positions = []
    fill_positions(root, 0, width // 2, positions, width // 2)

    # Place nodes in grid
    for depth, pos, value in positions:
        grid[depth * 2][int(pos)] = str(value)
        if depth * 2 + 1 < height * 2:
            current_shift = width // (2 ** (depth + 2))
            # Check if left child exists
            if any((d, int(pos - current_shift)) == (depth + 1, p) for d, p, _ in positions):
                grid[depth * 2 + 1][int(pos - current_shift)] = "/"
            # Check if right child exists
            if any((d, int(pos + current_shift)) == (depth + 1, p) for d, p, _ in positions):
                grid[depth * 2 + 1][int(pos + current_shift)] = "\\"

    # Print grid
    for row in grid:
        print("".join(row))

preorderList = []
inorderList = []
postorderList = []

def preorder(node):
    if node is None:
        return None
    preorderList.append(node.value)
    preorder(node.left)
    preorder(node.right)
def inorder(node):
    if node is None:
        return None
    inorder(node.left)
    inorderList.append(node.value)
    inorder(node.right)

def postorder(node):
    if node is None:
        return None
    postorder(node.left)
    postorder(node.right)
    postorderList.append(node.value)



def main():
    validAnswers = ["pre", "in", "post", "x"]
    run = True
    while run:
        preorderList.clear()
        inorderList.clear()
        postorderList.clear()
        order = (input("type either 'pre', 'in', or 'post' for type of traversal, or 'x' to quit: ")).lower()
        while order not in validAnswers:
            print("Incorrect input! please review the options and type accordingly")
            order = (input("type either 'pre', 'in', or 'post' for type of traversal, or 'x' to quit: ")).lower()
        if order == "x":
            print("Goodbye!")
            break
        size = int(input("select size of tree: "))
        tree = generate_random_tree(size)
        print_tree_2d(tree)
        sequence = input("type the sequence of numbers in your selected order with spaces between: ")
        while not sequence.replace(" ", "").isnumeric():
            print("make sure sequence only contains numbers")
            sequence = input("type the sequence of numbers in your selected order with spaces between: ")
        seqList = sequence.split()
        res = [eval(i) for i in seqList]
        if order == "pre":
            preorder(tree)
            if res == preorderList:
                print("Correct! you have done a correct preorder traversal!")
            else:
                print("Incorrect! the correct traversal is:", preorderList)
        elif order == "in":
            inorder(tree)
            if res == inorderList:
                print("Correct! you have done a correct inorder traversal!")
            else:
                print("Incorrect! the correct traversal is:", inorderList)
        elif order == "post":
            postorder(tree)
            if res == postorderList:
                print("Correct! you have done a correct postorder traversal!")
            else:
                print("Incorrect! the correct traversal is:", postorderList)
main()


