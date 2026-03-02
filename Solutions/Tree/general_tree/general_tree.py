class node:
    def __init__(self, data):
        self.data = data
        self.depth = 0
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        child.depth = self.depth + 1
        self.children.append(child)

    def get_level_cpu(self):
        depth = 0
        p = self.parent
        while p:
            depth += 1
            p = p.parent
        return

    def print_tree(self):
        prefix = (" " * self.depth * 3) + "|__" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print_tree()

def fill_tree():
    root = node("Nilupul (CEO)")
    cto = node("Chinmay (CTO)")
    root.add_child(cto)
    infrastructure = node("Vishwa (Infrastructure Head)")
    cto.add_child(infrastructure)
    infrastructure.add_child(node("Dhaval (Cloud Manager)"))
    infrastructure.add_child(node("Abhijit (App Manager)"))
    cto.add_child(node("Aamir (Application Head)"))
    
    hr = node("Gels (HR Head)")
    root.add_child(hr)
    hr.add_child(node("Peter (Recruitment Manager)"))
    hr.add_child(node("Waqas (Policy Manager)"))

    return root

tree = fill_tree()

tree.print_tree()