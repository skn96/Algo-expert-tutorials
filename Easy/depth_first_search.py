# T ; O(V+E)
# S : O(V)

class Node: 
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name): 
        self.children.append(Node(name))

    def depthFirstSearch(self, array): 
        array.append(self.name)
        for child in self.children: 
            self.depthFirstSearch(self, array)
        return array