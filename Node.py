class TrieNode:
    def __init__(self, prefix=None, parent=None, is_word=False):
        """

        :param prefix: prefix of this node
        :param parent: parent node in the trie
        :param is_word: True if the node stores a node
        """
        self.prefix = prefix
        self.children = dict()
        self.parent = parent
        self.count = 0      
        self.top_results = Counter()
        if is_word:
            self.top_results[self.prefix] = 1
        self.isWord = is_word

    def __delete_helper(self, node):
        """
        Breadth-first search to find all children nodes that are words
        :param node: TrieNode, subtree root
        :return: set(str)
        """
        q = deque([node])
        res = set()
        while q:
            cur = q.popleft()
            if cur.isWord:
                res.add(cur.prefix)
            for _, child in cur.children.items():
                q.append(child)
        return res

    @staticmethod
    def __search_helper(word_list, idx, path, res):
        if idx == len(word_list):
            res.append(list(path))
            return
        for word in word_list[idx]:
            path.append(word)
            Server.__search_helper(word_list, idx+1, path, res)
            path.pop()