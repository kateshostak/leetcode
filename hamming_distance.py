class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
       return sum(map(int,format(x^y, 'b')))
