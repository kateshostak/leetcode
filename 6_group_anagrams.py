from typing import List
from collections import Counter
import pdb


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        is_marked = [0]*len(strs)
        for i in range(len(strs)):
            if not is_marked[i]:
                tmp_i = Counter(strs[i])
                tmp_angr = [strs[i]]
                is_marked[i] = 1
            else:
                continue
            for j in range(i + 1, len(strs)):
                tmp_j = Counter(strs[j])
                if tmp_i == tmp_j:
                    tmp_angr.append(strs[j])
                    is_marked[j] = 1
            anagrams.append(tmp_angr)
        return anagrams


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # strs = ["",""]
    s = Solution()
    res = s.groupAnagrams(strs)
    print(res)


if __name__ == '__main__':
    main()
