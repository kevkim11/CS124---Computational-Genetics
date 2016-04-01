def string_slicer(s, a, b, c, d):
    """
    :param a, b: A string s of length at most 200 letters and four integers a, b, c and d.
    :return: The slice of this string from indices a through b and c through d (with space in between), inclusively.
    """
    return s[a:b+1]+" "+s[c:d+1]

if __name__ == "__main__":
    s = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain"
    ans = string_slicer(s, 22, 27, 97, 102)
    t = "LrLButasturQZpixjZ4HAmD8MSOEVvll0YxKi0RdTq7uJB982aHK0z838gtvGxZCcwsWqGvpkBI71fVHmGoVp8hnBsli7jkx9xZmTG8SHiyUihcj4pW7ANeP3dPzbVsl8F09cXkb3LbEHKktKOcD6D6IG3e8hMIBl35nlihCnAffIVeelegansiru4"
    ans2 = string_slicer(t, 3, 10, 175, 181)
    print ans
    print ans2



