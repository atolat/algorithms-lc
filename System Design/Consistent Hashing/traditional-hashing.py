import hashlib
# Define a storage node
class Node:
    def __init__(self, name, host):
        self._name = name
        self._host = host

    def put(self, path):
        # Store
        pass

    def fetch(self, path):
        # Retrieve 
        pass


# Instances of storage nodes
storage_nodes = [
    Node('A', '10.131.213.12'),
    Node('B', '10.131.213.12'),
    Node('C', '10.131.213.12'),
    Node('D', '10.131.213.12'),
    Node('E', '10.131.213.12')
]

def hash_fn(key):
    '''
    Returns the hash of the key -> 0 to 4
    '''
    return hash(key) % 5

def upload(path):
    # Get the index of the storage node
    index = hash_fn(path)
    # Get the instance of the node and upload the file
    node = storage_nodes[index]
    return node.put(path)

def fetch(path):
     # Get the index of the storage node
    index = hash_fn(path)
    # Get the instance of the node and fetch the file from the node and return
    node = storage_nodes(index)
    return node.fetch(path)