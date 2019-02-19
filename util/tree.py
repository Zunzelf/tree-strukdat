class Node(object):
    # leaf.node class

    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.childPnt  = []

    def find(self, name, retChild = False):
        inp = list(name[::-1])
        return self.trace(inp, retChild)

    def trace(self, inp, retChild):
        if len(inp) == 0 and self.val == "$":
            if self.left is not None:
                if retChild:
                    ls = []
                    self.getChild(ls)
                    return ls
                return self.left.val
            return True
        elif len(inp) == 0 and self.val != "$":
            return False
        else :
            if len(inp) > 0:
                x = inp.pop()
                if(self.val == x.lower()):
                   return self.left.trace(inp, retChild)
                if(self.val != x.lower()):
                    if self.right is not None :
                        inp.append(x)
                        return self.right.trace(inp, retChild)
                    else :
                        return False

    def insert(self, name, m = "", child = []):
        inp = list(name)
        self.add(inp, m, child)
    
    def add(self, inp, m = "", child = []):
        if len(inp) > 0:
            x = inp.pop()
            if self.val != x.lower():
                if self.right is None:
                    self.right = Node(x)
                inp.append(x)
                self.right.add(inp, m, child)
            if self.val == x.lower():
                if len(inp) > 0:
                    x = inp.pop()
                    if self.left is None:
                        self.left = Node(x)
                    inp.append(x)
                    self.left.add(inp, m, child)
                else:
                    blank = Node("$")
                    if m != "":
                        blank.left = Node(m)
                    if len(child) > 0:
                        chl = Node(child.pop())
                        chl.insertChild(child)
                        blank.left = chl
                        ls = []
                        blank.getChild(ls)
                    self.left = blank
    # child utils
    def insertChild(self, inp):
        if len(inp) > 0:
            self.right = Node(inp.pop())
            self.left = Node("$")
            self.right.insertChild(inp)

    def getChild(self, ls = []):
        if self.left is not None:
            if self.left.val !="$":
                ls.append(self.left.val)
                self.left.getChild(ls)
            elif(self.right is not None):
                ls.append(self.right.val)
                self.right.getChild(ls)

    # lang structure check
    def check(self, inp):
        inp_ls = list(inp.split(" "))
        res = False
        res = self.checks(inp_ls[::-1])
        return res

    def checks(self, inp):
        pnt = inp.pop()
        res = self.find(pnt, True)
        rsl = False
        if res :
            if len(inp) == 0:
                if res:
                    rsl = True
            else:
                pnt = inp.pop()
                if type(res) != type(True):
                    res = [x for x in res if x == pnt]
                else :
                    res = []
                if len(res) > 0 :
                    inp.append(pnt)
                    rsl = self.checks(inp)
                else:
                    rsl = False
        return rsl

class Tree(object):
    def __init__(self, root = 0):
        self.root = Node(root)

    def generate(self, values):
        for val in values:
            self.root.insert(val[::-1])

    def insert(self, val, child = []):
        self.root.insert(val[::-1], child = child)

    def generateDict(self, dicts, text = "text", means = "arti"):
        for val in dicts:
            self.root.insert(val[text][::-1], val[means])

    def generateRef(self, dicts, text = "val", childs = "next"):
        for val in dicts:
            self.root.insert(val[text][::-1], child = val[childs])

    def find(self, inp):
        if self.root.find(inp):
            return True
        else :
            False
    def check(self, inp):
        return self.root.check(inp)

if __name__ == '__main__':
    eod = Node("$", )
    sample = [
        "ab",
        "abz",
        "acd",
        "bkt",
        "bs",
        "bss",
        "cmyk"
    ]

    a = {
    'val' : "makan",
    'next' : ["ayam", "soto", "daging"]
    }

    b = {
        'val' : "ayam",
        'next' : []
    }

    c = {
        'val' : "soto",
        'next' : ["ayam"]
    }

    kms = [a, b, c]

    sample_tree = Tree()
    # sample_tree.generate(sample)
    # sample_tree.insert(a['val'], child = a["next"])
    # sample_tree.insert(c['val'], child = c["next"])
    # sample_tree.insert(b['val'], child = b["next"])

    sample_tree.generateRef(kms)
    print(sample_tree.check("makan soto ayam"))
    print(sample_tree.check("ayam"))
    print(sample_tree.check("soto"))
    # print(sample_tree.check("makan soto"))
    # print(sample_tree.check("makan bebek"))
    print(sample_tree.find("ayam"))
    print(sample_tree.find("soto"))
    print(sample_tree.find("makan"))
