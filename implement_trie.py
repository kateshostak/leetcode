import string


class Node:
    def __init__(self):
        self.children = {letter: None for letter in string.ascii_lowercase}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        tmp = self.root
        i = 0
        while i < len(word):
            if not tmp.children[word[i]]:
                tmp.children[word[i]] = Node()
            tmp = tmp.children[word[i]]
            i += 1
        tmp.end_of_word = True

    def search(self, word: str) -> bool:
        tmp = self.root
        i = 0
        while i < len(word):
            if tmp.children[word[i]]:
                tmp = tmp.children[word[i]]
                i += 1
            else:
                return False
        if not tmp.end_of_word:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        tmp = self.root
        i = 0
        while i < len(prefix):
            if tmp.children[prefix[i]]:
                tmp = tmp.children[prefix[i]]
                i += 1
            else:
                return False
        return True


def main():
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    print(trie.search("apple"))
    print(trie.search("app"))

    trie = Trie()
    print(trie.startsWith("a"))


if __name__ == '__main__':
    main()
