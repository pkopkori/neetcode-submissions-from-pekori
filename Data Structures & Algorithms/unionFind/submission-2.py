class UnionFind:
    
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        self.num_components = n

        for i in range(0, n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        p = self.par[x]
        while p != self.par[p]:
            p = self.par[self.par[p]]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)
        return p1 == p2

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y):
            return False

        p1, p2 = self.find(x), self.find(y)
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
             self.par[p2] = p1
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        self.num_components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_components

