calls = 0

def count_calls():
    global calls
    calls +=1


def string_info():
     count_calls()
     str_= input ('введите слово, начинающееся с большой буквы:')
     tuple_ = (len(str_), str_.upper(), str_.lower())
     print(tuple_)


def is_contains():
    count_calls()
    str_ = input('введите слово:')
    print ('сейчас вы создадите список')
    n = int(input('введите желаемое количество элементов списка'))
    i = 0
    list_=[]
    while i < n:
        el_= input(f'введите элемент списка № {i+1}')
        list_.append(el_)
        i += 1
    print(str_ in list_)


string_info()
is_contains()
print(calls)