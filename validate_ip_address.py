class Solution:
    def validIPAddress(self, IP: str) -> str:
        packs = IP.split('.')
        packs_2 = IP.split(':')
        if len(packs) == 4 and self.check_ipv4(packs):
            return "IPv4"
        elif len(packs_2) == 8 and self.check_ipv6(packs_2):
            return "IPv6"
        else:
            return "Neither"

    def check_ipv6(self, packs):
        pass

    def len_is_roght(self, pack):
        return len(pack) < 4

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
        return pack[0] == 0

    def negative_number(self, pack):
        return pack[0] == '-'

    def less_than_256(self, pack):
        return int(pack) >= 256


def main():
    ip = "172.16.254.1"
    res = Solution().validIPAddress(ip)
    print(f'expected::IPv4, got::{res}')


if __name__ == '__main__':
    main()
