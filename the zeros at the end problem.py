
a = [0,1,2,6,8,0,6,7,9,0,4]

x = a.count(0)

while x > 0:
    a.remove(0)
    a.append(0)
    x -= 1
    print(a)

print(a)
