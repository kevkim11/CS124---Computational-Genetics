import math

def hypotenuse_square(a, b):
    """
    :param a, b: Two positive integers a and b, each less than 1000.
    :return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.
    """
    return math.pow(a, 2)+math.pow(b, 2)

if __name__ == "__main__":
    a = 839
    b = 957
    ans = hypotenuse_square(a, b)
    print ans
