"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        dict_ = {}
        self.buildDictionary(node, dict_)
        
        for n in dict_.keys():
            for c in n.neighbors:
                dict_[n].neighbors.append(dict_[c])
                
        return dict_[node]
            
    def buildDictionary(self, node, dict_:dict()) -> None:
        stack = []
        stack.append(node)
        
        while stack:
            cur = stack.pop()
            dict_[cur] = Node(cur.val, [])
            
            for c in cur.neighbors:
                if c not in dict_.keys():
                    stack.append(c)
        return
