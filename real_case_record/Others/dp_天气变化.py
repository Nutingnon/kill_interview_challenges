# 问题描述：
# 如果我们把天气分为雨天，阴天和晴天3种，在给定各种天气之间转换的概率，例如雨天转换成雨天，
# 阴天和晴天的概率分别为0.4,0.3,0.3.那么在雨天后的第二天出现雨天,阴天和晴天的概率分别为0.4,0.3,0.3.
# 现在给你今天的天气情况,问你n天后的某种天气出现的概率.

# 输入样例：
# 我们这里假设1,2,3分别代表3种天气情况,Pij表示从i天气转换到j天气的概率. 首先是一个数字T表示数据的组数.
# 每组数据以9个数开始分别是P11,P12,P13,……,P32,P33,接着下一行是一个数字m，表示提问的次数。每次提问有3个数据，
# i,j,n,表示过了n天从i天气情况到j天气情况(1<=i,j<=3 1<=n<=1000)。


# 输出要求：
# 根据每次提问输出相应的概率(保留3位小数)。
# 具体例子：
# Input
# 1 0.4 0.3 0.3 0.2 0.5 0.3 0.1 0.3 0.6 3 1 1 1 2 3 1 1 1 2
# Output：
# 0.400 0.300 0.250

# 1 rain, 2 cloudy, 3 sunshine

# def predict_next_day(x):
#     if x == 1:
#         return ((1,0.4),(2,0.3),(3,0.3))
#     elif x == 2:
#         return ((1,0.2),(2,0.5),(3,0.3))
#     elif x == 3:
#         return ((1,0.1),(2,0.3),(3,0.6))

def recursive_func1(x):
    x = x.split(' ')
    for i in range(len(x)):
        if '.' in x[i]:
            x[i] = float(x[i])
        else:
            x[i] = int(x[i])
    probility_list = x[1:10]
    groups = x[10]
    q = []
    # record the question
    for i in range(groups):
        q.append(x[11+3*i:11+3*i+3])
    print('q is :',q)

    answer = []
    for f in q:
        previous_day = [[f[0], 1]]
        for ff in range(f[2]):
            previous_day = recursive_func2(previous_day,probility_list)
        answer.append(round(previous_day[f[1]-1][1],3))
    return answer

def recursive_func2(previous_day,prob_form):
    # 前一种状态只可能有三种情况，分别算出三种情况推出的各种情况，然后相加得到下一天的数据
    record2nextday = [[],[],[]]
    if len(previous_day) == 1:
        next_day = [[1,prob_form[3*(previous_day[0][0])-3]],[2,prob_form[3*(previous_day[0][0])-2]],[3,prob_form[3*(previous_day[0][0])-1]]]
    else:
        for i in previous_day:
            if i[0] == 1:
                record2nextday[0].append(i[1]*prob_form[0])
                record2nextday[1].append(i[1]*prob_form[1])
                record2nextday[2].append(i[1]*prob_form[2])
            elif i[0] == 2:
                record2nextday[0].append(i[1]*prob_form[3])
                record2nextday[1].append(i[1]*prob_form[4])
                record2nextday[2].append(i[1]*prob_form[5])
            elif i[0] == 3:
                record2nextday[0].append(i[1]*prob_form[6])
                record2nextday[1].append(i[1]*prob_form[7])
                record2nextday[2].append(i[1]*prob_form[8])

        next_day = [sum(t) for t in record2nextday]
        next_day = [[n+1,m] for n,m in enumerate(next_day)]
    return next_day






print(recursive_func1('1 0.4 0.3 0.3 0.2 0.5 0.3 0.1 0.3 0.6 3 1 1 1 2 3 1 1 1 2'))
