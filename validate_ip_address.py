class Solution:
    def validIPAddress(self, IP: str) -> str:
        packs = IP.split('.')
        packs_2 = IP.split(':')
        if len(packs) == 4 and self.check_ipv4(packs):
            return "IPv4"
        elif len(packs_2) == 8:
            return self.check_ipv6(packs_2)
        else:
            return "Neither"

    def check_ipv4(self, packs):
        flag = True
        for pack in packs:
            flag &= self.leading_zero(pack)
        if not flag:
            return False

        for pack in packs:
            flag &= self.negative_number(pack)
        if not flag:
            return False

        for pack in packs:
            flag &= self.less_than_256(pack)
        if not flag:
            return False
        return True

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
