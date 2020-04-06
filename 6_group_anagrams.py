from typing import List
from collections import Counter
import pdb


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            tmp = self.letter_counter(word)
            if tmp in anagrams:
                anagrams[tmp].append(word)
            else:
                anagrams[tmp] = [word]
        return list(anagrams.values())

    def letter_counter(self, word):
        tmp = Counter(word)
        s = ''
        for l in sorted(tmp):
            s += l + str(tmp[l])
        return s


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    res = s.groupAnagrams(strs)
    print(res)


if __name__ == '__main__':
    main()
