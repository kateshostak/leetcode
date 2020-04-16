import pdb


class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = 0
        sum_ = 0
        stars = self.count_stars(s)
        stars_pref = 0
        stars_suff = stars
        symbol_i =0
        star_i = 0
        for i, symbol in enumerate(s):
            if symbol == '(':
                symbol_i = i
                sum_ += 1
            elif symbol == ')':
                symbol_i = i
                sum_ -= 1
            else:
                star_i = i
                stars_pref += 1
                stars_suff -= 1

            if sum_ < 0:
                if stars_pref > 0:
                    sum_ += 1
                    stars_pref -= 1
                else:
                    return False

        if sum_ == 0:
            return True
        else:
            if sum_ == star_i - symbol_i:
                return True
        return False

    def count_stars(self, s):
        return sum([1 for symbol in s if symbol == '*'])
def main():
    # Input: "()"
    # Output: True

    # Input: "(*)"
    # Output: True

    # Input: "(*))"
    # Output: True
    s = ''
    print(Solution().checkValidString(s))


if __name__ == '__main__':
    main()
