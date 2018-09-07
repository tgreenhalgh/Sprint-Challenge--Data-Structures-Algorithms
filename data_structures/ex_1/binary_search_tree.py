class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        # execute the callback with this node's value
        cb(self.value)
        # start going down the left side
        if self.left:
            self.left.depth_first_for_each(cb)
        # then go down the right side
        if self.right:
            self.right.depth_first_for_each(cb)

    def breadth_first_for_each(self, cb):
        # setup a list of nodes to visit
        to_visit = [self]

        # keep going as long as we have nodes
        while to_visit:
            # get the first node from our list
            node = to_visit.pop(0)
            # add the left node if we have one
            if node.left:
                to_visit.append(node.left)
            # add the right node if we have one
            if node.right:
                to_visit.append(node.right)
            # execute the callback with this node's value
            cb(node.value)

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
