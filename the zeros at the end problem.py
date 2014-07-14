
# initial list
a = [0,1,2,6,8,0,6,7,9,0,4]

# countdown variable
x = a.count(0)

# while loop will continually remove and append
# 0's until our intital count value of the number
# of zeroes reaches 0
while x > 0:
    a.remove(0)
    a.append(0)
    x -= 1
    print(a)


