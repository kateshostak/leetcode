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

    def len_is_right(self, pack):
        return len(pack) < 4

    def check_cond(self, func_name, packs):
        return all(getattr(self, func_name)(pack) for pack in packs)

    def check_ipv4(self, packs):
        for pack in packs:
            if pack[0] == 0 or pack[0] == '-' or int(pack) >= 256:
                return False
        return True

    def leading_zero(self, pack):
        return pack[0] != 0

    def negative_number(self, pack):
        return pack[0] != '-'

    def less_than_256(self, pack):
        return int(pack) < 256


def main():
    ip = "172.16.254.1"
    res = Solution().validIPAddress(ip)
    print(f'expected::IPv4, got::{res}')


if __name__ == '__main__':
    main()
