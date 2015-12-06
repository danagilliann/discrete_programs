def extended_euclid(a,b):
    if b == 0:
        return (a,1,0)
    (d2,x2,y2) = extended_euclid(b, a % b)
    d = d2
    x = x2
    y = x2 - (a/b)*y2
    return (d,x,y)

print extended_euclid(540,52)
