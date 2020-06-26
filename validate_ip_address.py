import string


class Solution:

    def validIPAddress(self, IP: str) -> str:
        NEITHER = "Neither"
        IPV4 = "IPv4"
        IPV6 = "IPv6"

        if '.' in IP:
            return IPV4 if self.is_ipv4(IP) else NEITHER

        if ':' in IP:
            return IPV6 if self.is_ipv6(IP) else NEITHER

        return NEITHER

    def is_ipv6(self, ip):
        parts = ip.split(':')

        if len(parts) != 8:
            return False

        for part in parts:
            if len(part) > 4 or len(part) == 0:
                return False

            if not all(letter in string.hexdigits for letter in part):
                return False

        return True

    def is_ipv4(self, ip):
        parts = ip.split('.')

        if len(parts) != 4:
            return False

        for part in parts:
            if len(part) == 0:
                return False

            if part[0] == '0' and len(part) > 1:
                return False

            if not part.isdigit():
                return False

            if int(part) >= 256:
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

    ip = "01.01.01.01"
    res = Solution().validIPAddress(ip)
    print(f'expected::Neither, got::{res}')

    ip = "20EE:FGb8:85a3:0:0:8A2E:0370:7334"
    res = Solution().validIPAddress(ip)
    print(f'expected::Neither, got::{res}')

    ip = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    res = Solution().validIPAddress(ip)
    print(f'expected::IPv6, got::{res}')

    ip = "1122.123.123.123"
    res = Solution().validIPAddress(ip)
    print(f'expected::Neither, got::{res}')


if __name__ == '__main__':
    main()
