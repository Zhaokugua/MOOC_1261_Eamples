#班里考试后，老师要统计几位同学的平均成绩，已知5位同学的成绩用list表示如下：
#L = [75, 92, 59, 68, 99]
#请利用for循环计算出平均成绩。

# Enter a code
L = [75, 92, 59, 68, 99]
sum = 0.0
for i in L:
    sum = sum + i
print(sum/5)
