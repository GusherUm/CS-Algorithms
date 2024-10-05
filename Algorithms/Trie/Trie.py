from collections import defaultdict

# Let's say we are only dealing with Lowecase letters now

class Trie:

    def __init__(self):
        self.dic = defaultdict(Trie)
        self.isLast = [True]*26

    # Add
    def add(self, word):
        
        cur = self  

        for i in range(len(word)):
            if word[i] not in cur.dic.keys():
                cur.dic[word[i]] = Trie()
                cur.isLast[ord(word[i]) - 97] = False
            
            if i == len(word) - 1:
                cur.isLast[ord(word[i]) - 97] = True

            cur = cur.dic[word[i]]

    # Search
    def search(self, word):

        cur = self

        for i in range(len(word)):
            if word[i] not in cur.dic.keys():
                return False
            elif i != len(word) - 1 and cur.isLast[ord(word[i]) - 97] is True:
                return False
            elif i == len(word) - 1 and cur.isLast[ord(word[i]) - 97] is False:
                return False
            
            cur = cur.dic[word[i]]

        return True

x = Trie()
x.add('helloworld')

print(x.search('helloworld'))
print(x.search('hello'))