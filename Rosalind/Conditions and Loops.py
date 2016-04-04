
def expected_offspring(a, b):
    """
    :param s: A DNA string s of length at most 1000 nt.
    :return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
    """
    copy = b
    total=a
    for i in range(copy):
        if(total==a):
            i+=total
            print "jklasdfa"
        if(i%2==1):
            total+=i
        print "a="+ str(total)
    return

if __name__ == "__main__":
    expected_offspring(100, 200)
