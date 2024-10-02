def sum(list_):
    list_1 = []
    for i in list_:
        if type(i) == str or type(i) == int:
            list_1.append(i)
        if type(i) == list or type(i) == tuple or type(i) == set:
            list_1 += list(i)
        if type(i) == dict:
            list_1 += list(i.values()) + list(i.keys())
    n = True
    for i in list_1:
        if type(i) == list or type(i) == tuple or type(i) == dict or type(i) == set:
            n = False
            break
    sum_ = 0
    if n == True:
        for i in list_1:
            if type(i) == int:
                sum_ += i
            else:
                sum_ += len(i)
        return sum_
    else:
        return sum(list_1)


print (sum([[1,2,3],{'a':4, 'b':5},(6,{'cube':7,'drum':8}),'Hello',((),[{(2, 'urban', ('urban2',35))}])]))

#[[1,2,3],{'a':4, 'b':5},(6,{'cube':7,'drum':8}),'Hello',((),[{(2, 'urban', ('urban2',35))}])]