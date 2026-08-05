class node:
    def __init__(self, data, type):
        self.data = data
        self.type = type
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
        return depth

    def print_tree(self):
        prefix = (" " * self.get_level_cpu() * 3) + "|__" if self.parent else ""
        print(prefix + self.data + self.type)
        for child in self.children:
            child.print_tree()

def fill_tree():
    root = node("root", "/")
    home = node("home", "/")
    user = node("user", "/")
    documents = node("documents", "/")
    photos = node("photos", "/")
    guest = node("guest", "/")
    etc = node("etc", "/")
    var = node("var", "/")
    log = node("log", "/")
    tmp = node("tmp", "/")

    root.add_child(home)
    home.add_child(guest)
    home.add_child(user)
    user.add_child(documents)
    user.add_child(photos)
    guest.add_child(etc)
    guest.add_child(var)
    var.add_child(log)
    var.add_child(tmp)

    documents.add_child(node("resume", ".pdf"))
    documents.add_child(node("project", ".docx"))
    photos.add_child(node("img1", ".jpg"))
    photos.add_child(node("img2", ".png"))
    etc.add_child(node("config", ".yaml"))
    etc.add_child(node("hosts", ""))
    log.add_child(node("app", ".log"))
    log.add_child(node("error", ".log"))

    return root

tree = fill_tree()

tree.print_tree()