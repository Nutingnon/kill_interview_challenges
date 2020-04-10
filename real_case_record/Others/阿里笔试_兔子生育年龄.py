#
# 题目：
# 1. 猎人把一对兔子婴儿(一公一母称为一对)放到一个荒岛上，两年之后，它们生下一对小兔，之后开始每年都会生下一对小兔。生下的小兔又会以同样的方式继续繁殖。
# 2. 兔子的寿命都是x(x>=3)年，并且生命的最后一年不繁殖。
# 3. 如果岛上的兔子多于10对，那么猎人会每年在兔子们完成繁殖或者仙逝之后，从岛上带走两对最老的兔子。
# 请问y年(y>=3)后荒岛上所有的兔子加起来多少岁?(注意, 在条件3执行完之后)
#
# 输入: 从命令行输入两行整数，第一行是x，第二行是y
# 输出: y年后荒岛上所有的兔子岁数的总和

def rabit(x,y):
    # judge how many generation
    generation = int(y/2)
    record1 = []
    for i in range(generation):
        record1.append([])
    total_num = 0
    for j,k in enumerate(record1):
        if j == 0:
            record1[j].extend([1,0,'alive'])
            total_num += 1
        else:
            for l in range(j):
                # age up
                record1[l][1] += 2
                if record1[l][1] >=x:
                    record1[l][2] = 'dead'
            active_rabit = 0
            for m in record1[:j]:
                if m[2] == 'alive':
                    active_rabit+=m[1]

            record1[j].extend([active_rabit*2,0,'alive'])
            for n in record1[:j+1]:
                total_num += n[0]
            if total_num > 10:
                count = 0
                q = 0
                while q <= j and count <2:
                    if record1[q][0]>0:
                        record1[q][0] -=1
                        count +=1
                        continue
                    else:
                        q += 1
    sum_age =0
    for qq in record1:
        sum_age += qq[0]*qq[1]

    return sum_age,record1







print(rabit(4,6))





