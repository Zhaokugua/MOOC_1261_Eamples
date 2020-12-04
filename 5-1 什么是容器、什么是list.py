#Alice同学某次考试语文(Chinese)、数学(Math)、英语(English)三科的成绩分别是92、75、99，请使用list保存这些数据。
#注意：科目和成绩属于不同的数据类型。

# Enter a code
Subject = ['Chinese','Math','English']
Score = [92,75,99]
a = 0
for i in Subject:
    print(i + ":" +str(Score[a]))
    a = a + 1
