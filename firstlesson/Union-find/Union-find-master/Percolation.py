import random
import math
def Percolation(n):
    id = [];
    state = []  # id用来存放与i相连的编号
    opennums ,num = 0,0
    for i in range(n*n+1):
        id.append(i)
        state.append(0)
    state[n*n]=1    #let the extra element'state open
    flag = 1  # 没有渗透
    while (flag):
        state, id = openone(state, id, n)  # 随机将一个阻塞的块打开，返回状态向量，关联向量
        num+=1
        if (whetherpcn(id,state,n)):  # 判断打开后是否渗透
            opennums = num
            flag = 0
    property = opennums / (n * n)
    print("本次得到的概率是", property)
    return property


def openone(state, id, n):  # 用来打开一个site，并生成一颗树，即建立联系
    flag = 1
    while (flag):
        index = random.randint(0, n * n - 1)
        if (not state[index]):
            flag = 0
            state[index] = 1
    if (index!=n*n-1 and index%(n-1)!=0 and state[index + 1] == 1 ):
        id = Union(index, index + 1, id,n)
    if (index!=0 and index%(n)!=0 and state[index - 1] == 1 ):
        id = Union(index, index - 1, id,n)
    if (index<n*(n-1) and state[index + n] == 1 ):
        id = Union(index, index + n, id,n)
    if ( index>=n and state[index - n] == 1 ):
        id = Union(index, index - n, id,n)
    return state, id


def Union(p, q, id,n):  # Union()将两个相邻的格子相连其实是让这两个格子有相等的根节点，此处尽量让根节点大
    i = root(p, id, n)
    j = root(q, id, n)
    if (i == j):
        return id
    if (i < j):
        id[i] = j
    else:
        id[j] = i
    return id


def root(i, id, n):
    if (i < n * n and i >= n * (n - 1)):  # 最后n 个元素（底部元素）的权重值置 n×n
        id[i] = n * n
    while (i!=id[i]):
        id[i]=id[id[i]]
        i = id[i]
    return i


def whetherpcn(id,state, n):
    for i in range(n):
        if(state[i] == 1):
            if (root(i,id,n)==n*n):
                return 1
    return 0


def mean_stddev(n,times):
    #calculate the mean(average)
    oncep=0
    sumupp = 0
    listanswer=[]
    for i in range(times):
        oncep=Percolation(n)
        listanswer.append(oncep)
        sumupp += oncep
    mean=sumupp/times
    print("最后得到的平均值是",mean)
    stddev=0
    sumupp2=0
    for each in listanswer:
        sumupp2+=math.pow(each-mean,2)
    stddev=sumupp2/(times-1)
    stddev=math.sqrt(stddev)
    print("得到的方差是:",stddev)
    print("所以95%的置信区间为[",mean-(1.96*stddev)/math.sqrt(times)," , ",mean+(1.96*stddev)/math.sqrt(times) ,"]")


if "__name==__main__":
    mean_stddev(200,40)
