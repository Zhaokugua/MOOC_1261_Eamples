#五名同学的成绩可以用一个list表示：L = [95.5, 85, 59, 66, 72]，请按照索引的方式分别打印出第一名、第二名、第三名

# Enter a code
L = [95.5, 85, 59, 66, 72]
#冒泡排序，把成绩从大到小排列
i = 5
while i >= 0:
    j = 0
    while j < 4:
        if L[j] < L[j + 1]:
            L[j],L[j + 1] = L[j + 1],L[j]
        j = j + 1
    i = i - 1
#冒泡排序完成
print('First:' + str(L[0]) + '\nSecond:' + str(L[1]) + '\nThird:' + str(L[2]))


#其实python有可以自动排序的函数
#L.sort()     括号中reverse = True 是从大到小排序
