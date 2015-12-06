class color:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

def euclid(a,b):
    g = color.OKGREEN
    n = color.ENDC

    m = a % b

    if m == 0: # base case
        if b == 1: # relatively prime checker
            return g + str(b) + n
        else:
            return ""
    else:
        return euclid(b,m)

def implement_euclid(n):
    for i in range(1,n):
        print i
        print "\t", euclid(n,i)
    print n

def main():
    h = color.HEADER
    n = color.ENDC

    print "This program helps me understand Euler's Totient Function."
    c = int(input(h + "Enter a number to find all relatively prime numbers before it: " + n))
    implement_euclid(c)
    print "All the numbers that have a tabbed 1 printed on the number's next line is a relatively prime number"

main()
