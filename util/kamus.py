import os
import csv

class Node(object):
    # leaf.node class
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def find(self, name):
        inp = list(name[::-1])
        return self.trace(inp)

    def trace(self, inp):
        if len(inp) == 0 and self.val == "$":
            if self.left is not None:
                return self.left.val
            return True
        elif len(inp) == 0 and self.val != "$":
            return False
        else :
            if len(inp) > 0:
                x = inp.pop()
                if(self.val == x.lower()):
                   return self.left.trace(inp)
                if(self.val != x.lower()):
                    if self.right is not None :
                        inp.append(x)
                        return self.right.trace(inp)
                    else :
                        return False

    def insert(self, name, m = ""):
        inp = list(name)
        self.add(inp, m)
    
    def add(self, inp, m = ""):
        if len(inp) > 0:
            x = inp.pop()
            if self.val != x.lower():
                if self.right is None:
                    self.right = Node(x)
                inp.append(x)
                self.right.add(inp, m)
            if self.val == x.lower():
                if len(inp)>0:
                    x = inp.pop()
                    if self.left is None:
                        self.left = Node(x)
                    inp.append(x)
                    self.left.add(inp, m)
                else:
                    blank = Node("$")
                    if m != "":
                        blank.left = Node(m)
                    self.left = blank

class Tree(object):
    def __init__(self, root = 0):
        self.root = Node(root)

    def generate(self, values):
        for val in values:
            self.root.insert(val[::-1])

    def generateDict(self, dicts, text = "text", means = "arti"):
        for val in dicts:
            self.root.insert(val[text][::-1], val[means])

    def find(self, inp):
        return self.root.find(inp)

class Reader(object):
	def __init__(self, path = "kamus-raw.csv", binary = False):
		self.lsWord = self.load_csv_as_dict(path)
		self.tree = Tree()
		self.generateTree()

	def load_csv_as_dict(self, path, sep =","):
	    with open(path, "r") as file:
	        reader = csv.DictReader(file)
	        res = list(reader)
	        res = [dict(x) for x in res]
	    return res

	def translate(self, text, useTree = False):
		texts = []
		if not useTree:
			for txt in text.split(" "):
				res = [x["arti"] for x in self.lsWord if x["text"].lower() == txt.lower()]
				if len(res) > 0:
					texts.append(res[0])
				else:
					texts.append("...")
		else :
			for txt in text.split(" "):
				res = self.find(txt)
				if res:
					texts.append(res)
				else:
					texts.append("...")
		return " ".join(texts)

	def generateTree(self):
		# self.tree.generate([x['text'] for x in self.lsWord])
		self.tree.generateDict(self.lsWord)

	def find(self, inp):
		return self.tree.find(inp)


if __name__ == '__main__':
	path = os.path.join("..", "kamus-raw.csv")
	reader = Reader(path)
	inp = "aku makan"
	print(reader.translate(inp))
	print(reader.translate(inp, True))