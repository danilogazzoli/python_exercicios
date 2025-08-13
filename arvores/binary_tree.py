# Percorrimento (tree traversal) de árvore é o processo de visitar sistematicamente cada nó de uma árvore de dados, seguindo uma ordem específica, para ler, processar ou modificar esses nós.

# No caso de árvores binárias, os tipos mais comuns de percorrimento são:

# Pré-ordem (pre-order) – Visita primeiro o nó atual, depois o filho esquerdo e por último o filho direito.

# Em ordem (in-order) – Visita primeiro o filho esquerdo, depois o nó atual e por último o filho direito.

# Pós-ordem (post-order) – Visita primeiro o filho esquerdo, depois o direito e, por último, o nó atual.

# 💡 Em um Binary Search Tree (BST), o percorrimento em ordem retorna os valores ordenados automaticamente.

# Pre-order: Good for copying a tree or creating a prefix expression.

# In-order: Good for getting sorted data from a BST.

# Post-order: Good for deleting a tree or generating postfix expressions.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



#     10
#    /  \
#   5    20
#  / \   / 
# 3  7  15


# Create nodes
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(15)

#a) In-order (Left → Root → Right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

print("In-order traversal:")
inorder(root)

#b) Pre-order (Root → Left → Right)

def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

print("\nPre-order traversal:")
preorder(root)

#c) Post-order (Left → Right → Root)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")

print("\nPost-order traversal:")
postorder(root)

#4. Searching in a Binary Search Tree (BST)

def search(node, key):
    if node is None or node.value == key:
        return node
    if key < node.value:
        return search(node.left, key)
    return search(node.right, key)

result = search(root, 15)
print("\nFound:", result.value if result else "Not found")


## Binary Search Tree (BST)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
        # Ignore duplicates

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

# Example usage
bst = BinarySearchTree()
values_to_insert = [10, 5, 20, 3, 7, 15]
for v in values_to_insert:
    bst.insert(v)

print("In-order Traversal:", bst.inorder())


# SELECT AVG(salary)
# FROM employees
# WHERE department = 'IT';


# Execution happens in stages:

# 1 - Filter (department = 'IT')

# 2 - Aggregate (AVG)

# 3 - Output result

# We can model that as a tree where:

# * Root = Output step

# * Left child = Aggregate step

# * Right child = Data source

class QueryNode:
    def __init__(self, operation, data=None):
        self.operation = operation
        self.data = data  # optional metadata
        self.left = None
        self.right = None

    def execute(self):
        if self.operation == "SCAN":
            print(f"Scanning table: {self.data}")
        elif self.operation == "FILTER":
            if self.left:
                self.left.execute()
            print(f"Applying filter: {self.data}")
        elif self.operation == "AGGREGATE":
            if self.left:
                self.left.execute()
            print(f"Calculating aggregate: {self.data}")
        elif self.operation == "OUTPUT":
            if self.left:
                self.left.execute()
            print("Outputting result")

# Build query execution plan as a tree
root = QueryNode("OUTPUT")
root.left = QueryNode("AGGREGATE", "AVG(salary)")
root.left.left = QueryNode("FILTER", "department = 'IT'")
root.left.left.left = QueryNode("SCAN", "employees")

# Execute the query plan
root.execute()


class QueryNode:
    def __init__(self, operation, data=None):
        self.operation = operation
        self.data = data
        self.left = None
        self.right = None

class QueryPlanTree:
    def __init__(self):
        self.root = None

    def insert_root(self, operation, data=None):
        """Creates the root node."""
        self.root = QueryNode(operation, data)
        return self.root

    def insert_left(self, parent_node, operation, data=None):
        """Adds a node as the left child of a given parent."""
        parent_node.left = QueryNode(operation, data)
        return parent_node.left

    def insert_right(self, parent_node, operation, data=None):
        """Adds a node as the right child of a given parent."""
        parent_node.right = QueryNode(operation, data)
        return parent_node.right

    def execute(self):
        """Runs the query plan from the root."""
        self._execute_recursive(self.root)

    def _execute_recursive(self, node):
        if node is None:
            return
        
        if node.operation == "SCAN":
            print(f"Scanning table: {node.data}")
        elif node.operation == "FILTER":
            self._execute_recursive(node.left)
            print(f"Applying filter: {node.data}")
        elif node.operation == "AGGREGATE":
            self._execute_recursive(node.left)
            print(f"Calculating aggregate: {node.data}")
        elif node.operation == "OUTPUT":
            self._execute_recursive(node.left)
            print("Outputting result")

# Create the query plan
plan = QueryPlanTree()

root = plan.insert_root("OUTPUT")
agg = plan.insert_left(root, "AGGREGATE", "AVG(salary)")
flt = plan.insert_left(agg, "FILTER", "department = 'IT'")
scan = plan.insert_left(flt, "SCAN", "employees")

# Execute the plan
plan.execute()
