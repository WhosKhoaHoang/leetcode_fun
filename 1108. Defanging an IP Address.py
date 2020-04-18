class Solution:

    # Runtime: 24 ms
    # Memory: 13.9 MB
    def defangIPaddrReplace(self, address: str) -> str:
        return address.replace(".", "[.]")


    # Runtime: 32 ms
    # Memory: 13.9 MB
    def defangIPaddrJoin(self, address: str) -> str:
        return "[.]".join(address.split("."))


    # Runtime: 24 ms
    # Memory Usage: 13.7 MB
    def defangIPaddrLoop(self, address: str) -> str:
        res = ""
        for i in range(len(address)):
            if (i+1) < len(address) and address[i+1] == ".":
                res += address[i]+"["
            elif address[i] == ".":
                res += address[i]+"]"
            else:
                res += address[i]

        return res


if __name__ == "__main__":
    sol = Solution()
    addr = "1.1.1.1"

    res = sol.defangIPaddrReplace(addr)
    res = sol.defangIPaddrJoin(addr)
    res = sol.defangIPaddrLoop(addr)
    print(res)
