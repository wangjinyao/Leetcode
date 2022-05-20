# 写-个函数，输入是正奇数n，输出 1~n^2 的二维数组，要求1-1^2按一定规律排列。
# 例如，输入为7时，输出为
# 37  36  35  34  33  32  31  
# 38  17  16  15  14  13  30  
# 39  18  5   4   3   12  29  
# 40  19  6   1   2   11  28  
# 41  20  7   8   9   10  27  
# 42  21  22  23  24  25  26  
# 43  44  45  46  47  48  49

def solution(num):
    result = []
    if num == 1:
        return [[1]]
    elif num >1:
        pre_num = num-2
        tmp = solution(pre_num)

        # 第一行

        row1_index = pre_num**2+num-1
        # print(row1_index)
        row1 = list(range(row1_index, row1_index+num))[::-1]
        result.append(row1)
        start = row1[0]
        end = row1[-1]
        # 中间num-2行
        for x in range(len(tmp)):
            row = tmp[x]
            row.insert(0, start+1+x)
            row.append(end-1-x)
            result.append(row)
        # 最末一行
        rown = list(range(num**2-num+1, num**2+1))
        result.append(rown)
        return result
    else:
        raise

if __name__ == '__main__':
    num = 7
    result = solution(num)
    for row in result:
        for x in row:
            print(x, end='  ')
        print()