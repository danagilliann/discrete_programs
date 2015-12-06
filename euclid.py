def euclid(a,b):
    c = a % b
    if c == 0:
        if b == 1:
            print "\t", b
        return b
    else:
        euclid(b,c)

