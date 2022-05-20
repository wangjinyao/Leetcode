# 递归实现两个整数的乘积，要求不使用‘*’号（即乘号）

# def cheng(a, b):
#     result = 0
#     for x in range(a):
#         result += b
#     return result

# def cheng10(a):
#     return int(f'{str(a)}0')

# def solution(num1, num2):
#     num1_str = str(num1)

#     result = 0
#     for x in num1_str[::-1]:
#         a = cheng(x, num2)
#         result = cheng10(result)+a

# 递归
def solution(num1, num2):
    result = 0
    if num1>9:
        div, mod = divmod(num1, 10)
        tmp = solution(div, num2 )
        result = int(f'{str(tmp)}0') + solution(mod, num2)
    else:
        for _ in range(num1):
            result += num2

    return result

if __name__ == '__main__':
    num1 = 123
    num2 = 222
    result = solution(num1, num2)
    print(result, num1*num2)