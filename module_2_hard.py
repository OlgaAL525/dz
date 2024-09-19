n = int(input('Введите число от 3 до 20, которое показывает первое поле: '))
i=1
password_= []
while i < n:
    j=1
    while j < n:
        if n % (i+j) == 0 and i!=j:
            if i<j:
                x = str(i) + str(j)
                password_.append(x)
            else:
                x = str(j) + str(i)
                password_.append(x)
        j += 1
    i += 1

password_1 = list(dict.fromkeys(password_))

result=''
for i in password_1:
    result += str(i)

print('Чтобы выжить, вводи во второе поле: ',result)