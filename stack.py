#   Using stack to convert Infix to Postfix expression
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

ans = infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i")
print("To postfix = ", ans)

#   Using stack to convert Prefix to Infix expression

def PrefixToInfix(expression):
    #stack container
    stack = []
    #Reading the expression from right-to-left
    exp = expression[::-1]
    for char in exp:
        #Check for operand
        if char.isalnum():
            stack += char
        #Check for operator
        elif char=="(" or char==")" or char=="+" or char=="-" or char=="*" or char=="/":
            operand1 = stack.pop()
            operand2 = stack.pop()
            str = '(' + operand1 + char + operand2 + ')'
            stack.append(str)
    return stack.pop()


Ques = input("Enter prefix: ")
answer = PrefixToInfix(Ques)
print("Infix value is: ", answer)


#   Using stack to write an expression that balances brackets

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

print(Balanced_brackets("([{}])"))

# Find the Maximum Achievable Number
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
