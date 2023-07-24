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