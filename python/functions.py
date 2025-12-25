from basic import xyz

str=xyz.arr

def test():
    sum=0
    for i in xyz.arr2:
        sum+=i
    return sum

def test2():
    sum=" "
    for i in xyz.arr:
        sum+=i+" "
    return sum


print(test())
print(test2())