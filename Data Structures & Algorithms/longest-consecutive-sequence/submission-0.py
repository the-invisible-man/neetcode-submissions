class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        deduped = set(nums)

        uf = UnionFind(deduped)

        largest = 0

        for x in deduped:
            if x - 1 in deduped:
                uf.union(x, x -1)

            if x + 1 in deduped:
                uf.union(x, x + 1)

            size = uf.size_of(x)

            if size > largest:
                largest = size

        return largest

        
class UnionFind:

    def __init__(self, elements):
        self.elements = {el: i for i, el in enumerate(elements)}
        self.mappings = {i: i for i in range(len(elements))}
        self.size_tracker = [1] * len(elements)

    def union(self, el_1, el_2):
        parent_1 = self.get_parent(el_1)
        parent_2 = self.get_parent(el_2)

        if parent_1 == parent_2:
            # These components are already connected
            return

        size_1 = self.size_tracker[parent_1]
        size_2 = self.size_tracker[parent_2]

        if size_1 > size_2:
            # We join group 2 to group 1 as the parent
            self.mappings[parent_2] = parent_1
            self.size_tracker[parent_1] += self.size_tracker[parent_2]
        else:
            self.mappings[parent_1] = parent_2
            self.size_tracker[parent_2] += self.size_tracker[parent_1]

    def get_parent(self, el):
        target = self.elements[el]
        return self.get_root(target)

    def get_root(self, target):
        if target != self.mappings[target]:
            # Path compression for a O(α(n))
            self.mappings[target] = self.get_root(self.mappings[target])

        return self.mappings[target]

    def size_of(self, el):
        parent = self.get_parent(el)
        return self.size_tracker[parent]
