class Solution:
    def validIPAddress(self, IP: str) -> str:
        packs = IP.split('.')
        packs_2 = IP.split(':')
        if len(packs) == 4 and self.is_ipv4(packs):
            return "IPv4"
        elif len(packs_2) == 8 and self.is_ipv6(packs_2):
            return "IPv6"
        else:
            return "Neither"

    def is_ipv6(self, packs):
        for pack in packs:
            if len(pack) > 4 or len(pack) == 0 or pack[0] == '-' or not pack.isalnum():
                return False
        return True

    def is_ipv4(self, packs):
        for pack in packs:
            if pack[0] == 0 or pack[0] == '-' or int(pack) >= 256:
                return False
        return True


def main():
    ip = "172.16.254.1"
    res = Solution().validIPAddress(ip)
    print(f'expected::IPv4, got::{res}')

    ip = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    res = Solution().validIPAddress(ip)
    print(f'expected::IPv6, got::{res}')

    ip = "256.256.256.256"
    res = Solution().validIPAddress(ip)
    print(f'expected::Neither, got::{res}')


if __name__ == '__main__':
    main()
