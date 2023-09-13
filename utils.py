class utils:
    def reverser(decimal: int) -> int:
        r = 0
        while decimal > 0:
            r *= 10
            r += decimal % 10
            decimal //= 10
        return r
    def formatter(decimal: int):
        return oct(decimal), bin(decimal)