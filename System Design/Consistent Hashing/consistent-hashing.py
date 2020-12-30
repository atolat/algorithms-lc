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
    
def hash_fn(key, slots):
    hsh = hashlib.md5()
    hsh.update(bytes(key.encode('utf-8')))
    return int(hsh.hexdigest(), 16) % slots

class ConsistentHash:
    def __init__(self, slots):
       self._keys = []
       self._nodes = []
       self.slots = slots

    def add_node(self, node):
        key = hash_fn(node.host, self.slots)
        index = bisect(self._keys, key)
        self._nodes.insert(index, node)
        self._keys.insert(index, key)
        return key
    
    def remove_node(self, node):
        key = hash_fn(node.host, self.slots)
        index = bisect(self._keys, key)
        self._nodes.pop(index)
        self._keys.pop(index)
        return key
    
    def assign(self, item):
        key = hash_fn(item, self.slots)
        index = bisect_right(self._keys, key) % len(self._keys)
        return self.nodes[index]
