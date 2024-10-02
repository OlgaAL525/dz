def sum(*args):
    sum_ = 0
    for i in args:
        if  type(i) == int:
            sum_ += i
        if type(i) == str:
            sum_ += len(i)
        else:
            if type(i) == list or type(i) == tuple or type(i) == set:
                sum_ += sum(*list(i))
            if type(i) == dict:
                sum_ += (sum(*list(i.keys())) + sum(*list(i.values())))
    return sum_


print (sum([[1,2,3],{'a':4, 'b':5},(6,{'cube':7,'drum':8}),'Hello',((),[{(2, 'urban', ('urban2',35))}])]))
