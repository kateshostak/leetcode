import string


class Node:
    def __init__(self):
        self.children = {letter: None for letter in string.ascii_lowercase}
        self.end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
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

        def traverse(node, i):
            if i >= len(word):
                if node.end_of_word:
                    return True
                return False

            if word[i] == '.':
                for child in [elem for letter, elem in node.children.items() if elem is not None]:
                    if traverse(child, i + 1):
                        return True
                return False
            if not node.children[word[i]]:
                return False
            return traverse(node.children[word[i]], i + 1)
        return traverse(tmp, 0)


def main():
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")

    res1 = obj.search("pad")
    print(f'expected::False, got::{res1}')

    res1 = obj.search("bad")
    print(f'expected::True, got::{res1}')

    res1 = obj.search(".ad")
    print(f'expected::True, got::{res1}')

    res1 = obj.search("..d")
    print(f'expected::True, got::{res1}')

    res1 = obj.search("d..")
    print(f'expected::True, got::{res1}')

    res1 = obj.search("....")
    print(f'expected::False, got::{res1}')

    commands = ["addWord", "addWord", "addWord", "addWord", "search", "search", "addWord", "search", "search", "search", "search", "search", "search"]
    args = [["at"], ["and"], ["an"], ["add"], ["a"], [".at"], ["bat"], [".at"], ["an."], ["a.d."], ["b."], ["a.d"], ["."]]
    res = [None, None, None, None, False, False, None, True, True, False, False, True, False]
    obj = WordDictionary()
    i = 0
    for comm, arg in zip(commands, args):
        tmp = getattr(obj, comm)(*arg)
        print(f'expected::{res[i]}, got::{tmp}, word::{arg} ')
        i += 1


if __name__ == '__main__':
    main()
