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

# prefix = *+AB-CD and *-A/BC-/AKL
Ques = input("Enter prefix: ")
answer = PrefixToInfix(Ques)
print("Infix value is: ", answer)