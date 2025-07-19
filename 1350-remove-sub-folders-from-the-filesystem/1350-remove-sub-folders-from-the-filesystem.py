class TrieNode:
    def __init__(self):
        self.children={}
        self.eow=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def check(self,s):
        cur=self.root
        i=0
        while(i<len(s) and s[i] in cur.children):
            cur=cur.children[s[i]]
            i+=1
            if i==len(s):
                cur.eow=True
                return
            if cur.eow:
                return
        while(i<len(s)):
            cur.children[s[i]]=TrieNode()
            cur=cur.children[s[i]]
            i+=1
        cur.eow=True
        return
    def getAll(self):
        ans=[]
        def dfs(node,s):
            nonlocal ans
            if node.eow:
                ans.append(s[1:])
                return
            for v in node.children:
                dfs(node.children[v],s+"/"+v)
            return

        dfs(self.root,"")
        return ans
        



class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie=Trie()
        for f in folder:
            f=list(f.split("/"))
            trie.check(f)
        return trie.getAll()
        