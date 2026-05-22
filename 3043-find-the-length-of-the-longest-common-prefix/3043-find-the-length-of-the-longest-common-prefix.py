class TrieNode:
    def __init__(self):
        self.children = [None]*10

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,n):
        node=self.root
        strNum = str(n)
        for i in strNum:
            idx = int(i)
            if not node.children[idx]:
                node.children[idx]=TrieNode()
            node=node.children[idx]

    def find_longest(self, n):
        node=self.root
        cur=0
        for i in str(n):
            idx = int(i)
            if node.children[idx]:
                cur+=1
                node=node.children[idx]
            else:
                break
        return cur


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie=Trie()
        for num in arr1:
            trie.insert(num)
        ans=0
        for num in arr2:
            ans=max(ans, trie.find_longest(num))
        return ans