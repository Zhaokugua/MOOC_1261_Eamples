#请综合使用while和continue，计算0~1000以内，所有偶数的和。

# Enter a code
sum = 0
i = 0
while i <= 1000:
    i = i + 1
    if i % 2 == 1:
        continue
    sum = sum + i
print(sum)
