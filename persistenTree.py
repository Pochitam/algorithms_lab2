class Node:
    def __init__(self, value=0, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
    
class PersistentTree:
    def __init__(self, size):
        self.size = size
        if size <= 0:
            self.roots = [None]
        self.roots = [self.build(0, size-1)]

    def build(self, tl, tr):
        if tl > tr:
            return None
        if tl==tr: return Node()
        mid = (tl+tr)//2
        return Node(0, self.build(tl, mid), self.build(mid+1, tr))
    
    def update(self, tl, tr, l, r, prev_root, mark):
        if l>r or prev_root is None or tl > tr: return prev_root
        if tl == tr:
            new_node = Node(prev_root.value + mark, None, None)
            return new_node
        new_node = Node(prev_root.value, prev_root.left, prev_root.right)
        if tl>=l and tr<=r:
            new_node.value += mark 
            return new_node
        mid = (tr+tl)//2
        if l<=mid:
            new_node.left = self.update(tl, mid, l, r, prev_root.left, mark)
        if r > mid:
            new_node.right = self.update(mid+1, tr, l, r, prev_root.right, mark)
        return new_node
    
    def add_version(self, l, r, mark):
        prev_root = self.roots[-1]
        new_root = self.update(0, self.size-1, l, r, prev_root, mark)
        self.roots.append(new_root)
        return new_root
        

    def get(self, ind, tl, tr, node):
        if tr == tl: return node.value
        mid = (tl+tr)//2
        if ind<=mid:
            return node.value + self.get(ind, tl, mid, node.left)
        else:
            return node.value + self.get(ind, mid+1, tr, node.right)
        
    def get_ans(self, ind, version):
        node = self.roots[version]
        return self.get(ind, 0, self.size-1, node)