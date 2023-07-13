def infix_to_postfix(expression):
    # Function to determine the precedence of operators
    def precedence(operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        elif operator == '^':
            return 3
        else:
            return 0

    postfix = ''
    stack = []

    for char in expression:
        # If the character is an operand, append it to the postfix string
        if char.isalnum():
            postfix += char
        # If the character is an opening parenthesis, push it to the stack
        elif char == '(':
            stack.append(char)
        # If the character is a closing parenthesis, pop operators from the stack and append them to the postfix string until an opening parenthesis is encountered
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            # Pop the opening parenthesis from the stack
            if stack and stack[-1] == '(':
                stack.pop()
        else:
            # If the character is an operator, pop operators from the stack and append them to the postfix string until an operator with lower precedence is encountered
            while stack and stack[-1] != '(' and precedence(char) <= precedence(stack[-1]):
                postfix += stack.pop()
            # Push the current operator to the stack
            stack.append(char)

    # Pop any remaining operators from the stack and append them to the postfix string
    while stack:
        postfix += stack.pop()

    return postfix

def Balanced_brackets(exp):
    stack = []
    for i in exp:
        if i=="(" or i=="{" or i=="[":
            stack += i
        else:
            if not stack:
                print("No close brackets")
                return False
            cur_char = stack.pop()
            if cur_char == ")":
                if i != "(":
                    return False
            if cur_char == "]":
                if i != "[":
                    return False
            if cur_char == "}":
                if i != "{":
                    return False
    if stack:
        return False
    return True

# If A[i] == A[i - 2] and dp[i - 1] > 0
# extends the alternatice subarray
# then dp[i] = dp[i - 1] + 1

# else if A[i] == A[i - 1] + 1,
# starts the alternatice subarray
# dp[i] = 2

# else
# not in the alternatice subarray
# dp[i] = -1



# ❌Find the Maximum Achievable Number
class Solution:
    def alternatingSubarray(self, A: list[int]) -> int:
        n = len(A)
        res = dp = -1
        for i in range(1, n):
            if dp > 0 and A[i] == A[i - 2]:
                dp += 1
            else:
                if A[i] == A[i - 1] + 1:
                    dp = 2
                else:
                    -1
            res = max(res, dp)
        return res

result = Solution()
a = result.alternatingSubarray([ -5, -1, -1, 2, -2, -3 ])
print(a)
