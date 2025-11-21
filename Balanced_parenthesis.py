# balanced_parentheses.py
# Concept Program: Balanced Parentheses Checker (Stack)

def is_balanced(expression):
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}

    for ch in expression:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    print("🔎 Balanced Parentheses Checker")
    print("-------------------------------")

    exp = input("Enter an expression: ")

    if is_balanced(exp):
        print("Balanced ✔️")
    else:
        print("Not Balanced ❌")
