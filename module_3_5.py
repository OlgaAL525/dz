def get_multiplied_digits(namber):
    str_namber = str(namber)
    first = int(str_namber[0])
    if len(str_namber) == 1 or (len(str_namber) == 2 and str_namber[1:] == '0') :
        return first
    else:
        return first * get_multiplied_digits(int(str_namber[1:]))

result = get_multiplied_digits(8010)
print (result)