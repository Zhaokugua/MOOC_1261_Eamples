#请使用迭代的方式按顺序输出列表 L = ['Alice', 66, 'Bob', True, 'False', 100] 的偶数位置的元素。

# Enter a code
L = ['Alice', 66, 'Bob', True, 'False', 100] 
a = 0
for item in L:
    if a % 2 == 0:
        print(item)
    a = a + 1
