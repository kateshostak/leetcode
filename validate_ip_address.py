class Solution:
    def validIPAddress(self, IP: str) -> str:
        packs = IP.split('.')
        if len(packs) == 4:
            return self.check_ipv4(packs)

    def check_ipv4(self, packs):
        flag = True
        for pack in packs:
            flag &= self.leading_zero(pack)
        if not flag:
            return "Neither"

        for pack in packs:
            flag &= self.negative_number(pack)
        if not flag:
            return "Neither"

        for pack in packs:
            flag &= self.less_than_256(pack)
        if not flag:
            return "Neither"

        return "IPv4"

    def leading_zero(self, pack):
        if pack[0] == 0:
            return False
        return True

    def negative_number(self, pack):
        if pack[0] == '-':
            return False
        return True

    def less_than_256(self, pack):
        if int(pack) >= 256:
            return False
        return True


def main():
    ip = "172.16.254.1"
    res = Solution().validIPAddress(ip)
    print(f'expected::IPv4, got::{res}')


if __name__ == '__main__':
    main()
