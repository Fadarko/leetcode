class Solution:
    def summ(self, num):
        total = 0
        for number in num:
            total += number
        return total
    def dec(self, num:List[int], n: int):
        num[-1] += 1
    #    print(num)
        for i in range(0, len(num)):
            if num[-i] > n:
                if (num[-i - 1] != n - 1):
                    num[-i - 1] += 1
                    num[-i] = num[-i - 1] + 1
                else:
                    if len(num) > 2:
                        num[-i - 2] += 1
                        num[-i - 1] = num[-i - 2] + 1
                    num[-i] = num[-i - 1] + 1
    #        print(num)
        return num
    def combine(self, n: int, k: int) -> List[List[int]]:
        a = []
        ex = []
        x = []
        for i in range(1, k + 1):
            ex.append(i)
        a.append(ex)
        print(a)
        s = 0
        for i in range(n - k + 1, n + 1):
            s += i
        while self.summ(a[-1]) < s:
            x.extend(self.dec(a[-1], n))
            a.append(x[-3:])
            #print(x)
            print(a)
            print(str(self.summ(a[-1])) + "  -  " + str(s))
        print(x)
        return(a)

