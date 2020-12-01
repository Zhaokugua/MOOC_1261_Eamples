#请综合使用while True和break，计算0~1000以内，所有偶数的和。

# Enter a code
sum = 0
i = 2
while True:
    if i > 1000:
        break
    sum = sum + i
    i = i + 2
print(sum)
