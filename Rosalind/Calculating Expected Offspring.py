
def expected_offspring(a, b, c, d, e, f):
    """
    :param s: A DNA string s of length at most 1000 nt.
    :return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
    """
    return 2*((a)+(b)+(c)+(d*0.75)+(e*0.5)+(f*0))

if __name__ == "__main__":
    a=expected_offspring(19950, 18661, 19192, 17012, 19933, 19664)
    print a
