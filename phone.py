class Solution:
    def button(sels, butt: int) -> str:
        if butt == 2 :
            return(['a', 'b', 'c'])
        elif butt == 3:
            return(['d', 'e', 'f'])
        elif butt == 4:
            return(['g', 'h', 'i'])
        elif butt == 5:
            return(['j', 'k', 'l'])
        elif butt == 6:
            return(['m', 'n', 'o'])
        elif butt == 7:
            return(['p', 'q', 'r', 's'])
        elif butt == 8:
            return(['t', 'u', 'v'])
        elif butt == 9:
            return(['w', 'x', 'y', 'z'])
    def letterCombinations(self, digits: str) -> List[str]:
        sp_text = []
        if digits != '':
            sp_text = self.button(int(digits[0]))
            sp = []
            for i in range (1, len(digits)):
                text = self.button(int(digits[i]))
                sp.clear()
                for l_sp in sp_text:
                    for l_t in text:
                        sp.append(l_sp + l_t)
                sp_text.clear()
                sp_text.extend(sp)

        return(sp_text)