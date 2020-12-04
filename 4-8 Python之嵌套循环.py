#字符串s1='ABC'，字符串s2='123'，字符串s3='xyz'，请输出s1、s2、s3中所有字符的排列。

# Enter a code
s1 = 'ABC'
s2 = '123'
s3 = 'xyz'
for i in s1:
    for j in s2:
        for k in s3:
            print(i + j + k)
