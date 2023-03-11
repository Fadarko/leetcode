class Solution:
    def bracket(self, t: str, num: int) -> str:
        if num == 1:
            return ("(" + t + ")")
        elif num == 2:
            return (t + "()")
        elif num == 3:
            return ("()" + t)

    def generateParenthesis(self, n: int) -> List[str]:
        br = ["()"]
        for j in range(1, n):
            n_br = []
            for i in range(1, 4):
                for k in br:
                    t = self.bracket(k, i)
                    if (t not in n_br): n_br.append(t)
            br.clear()
            br.extend(n_br)
        if (n > 3): br.append("(())(())")
        return (br)
