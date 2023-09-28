# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            b_l = Bracket(char=next, position=i)
            opening_brackets_stack.append(b_l)
        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                print((i + 1))
                return i + 1
            top = opening_brackets_stack.pop()
            if not are_matching(top[0], next):
                print((i + 1))
                return i + 1
        else:
            pass
    if len(opening_brackets_stack) != 0:
        x = opening_brackets_stack[0]
        print(x[1] + 1)
        return x[1] + 1
    print("Success")
    return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
