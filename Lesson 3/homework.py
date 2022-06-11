# Bai 1
def isValid(s: str):

    dictionary = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack_arr = []

    for char in s:
        if char not in dictionary:
            stack_arr.append(char)
        else:
            if len(stack_arr) == 0 or stack_arr[-1] != dictionary[char]:
                return False
            else:
                stack_arr.pop(-1)

    return len(stack_arr) == 0

print(isValid("("))

# Bai 2
# def makeGood(s: str):

#     stack_arr = []

#     for char in s:
#         if char != stack_arr[-1] and char.lower() == stack_arr[-1]:
#             stack_arr.pop(-1)
#         else:
#             stack_arr.append(char)
    
#     return ''.join(stack_arr)

# print(makeGood("leeEetcode"))