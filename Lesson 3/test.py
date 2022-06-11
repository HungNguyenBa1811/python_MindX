# list_ans = []
# n = int(input("Input: "))

# def addParentheses(open: int, close: int, ans: str):
#     if open < n:
#         addParentheses(open + 1, close, ans + '(')
#     if open > close:
#         addParentheses(open, close + 1, ans + ')')
#     if open == n and close == n:
#         list_ans.append(ans)

# ans = ''
# addParentheses(0,0,ans)
# print(list_ans)





# Stack

input = '324*+'

def pushStack(stack_arr: list, num: int) -> None:
    stack_arr.append(num)
    return

def popStack(stack_arr: list) -> int:
    num_return = stack_arr[-1]
    stack_arr.pop(-1)
    return num_return

def calc(x: int, y: int, prefix: str):
    if prefix == '+':
        return x + y
    elif prefix == '-':
        return y - x
    elif prefix == '*':
        return x * y
    elif prefix == '/':
        return y / x

def prefix(input: str):
    stack_arr = []
    for char in input:
        if char.isdigit() == True:
            pushStack(stack_arr,int(char))
        else:
            x = popStack(stack_arr)
            y = popStack(stack_arr)
            ans = calc(x,y,char)
            pushStack(stack_arr,ans)
    
    return stack_arr[0]

print(prefix(input))