# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", r"{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            b = Bracket(next, i+1)
            opening_brackets_stack.append(b)


        if next in ")]}":
            if opening_brackets_stack and not are_matching(opening_brackets_stack[-1][0], next):
                return i+1
            elif opening_brackets_stack:
                opening_brackets_stack.pop(-1)
            else:
                return i+1
    if opening_brackets_stack:
        return opening_brackets_stack[-1][1]
    else:
        return "Success"


def main():
    text = input()
    print(find_mismatch(text))

    


if __name__ == "__main__":
    main()
