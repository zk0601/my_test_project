class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 1:
            return tokens[0]
        calculate_signs = ['+', '-', '*', '/']
        index = 0
        while True:
            if tokens[index] in calculate_signs:
                tokens[index] = self.func(tokens[index - 2], tokens[index - 1], tokens[index])
                tokens.pop(index - 2)
                tokens.pop(index - 2)
                if len(tokens) == 1:
                    return tokens[0]
                index = 0
                print(tokens)
            else:
                index += 1

    def func(self, num1, num2, sign):
        num1 = int(num1)
        num2 = int(num2)
        if sign == '+':
            return num1 + num2
        if sign == '-':
            return num1 - num2
        if sign == '*':
            return num1 * num2
        if sign == '/':
            return num1 // num2


if __name__ == '__main__':
    a = Solution()
    a.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
