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
print(Balanced_brackets("([{})"))