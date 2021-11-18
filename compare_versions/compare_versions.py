def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
# split our strings using . and change type from string to int.
    s1 = [int(i) for i in version1.split(".")]
    s2 = [int(i) for i in version2.split(".")]

# If we have lists of different length, let us add zeros to the end of short list.
    l1, l2 = len(s1), len(s2)
    if l1 < l2: s1 += [0]*(l2-l1)
    else: s2 += [0]*(l1 - l2)

#Finally, we need to compare s1 and s2 as lists.If s1 > s2 then we have 1-0 = 1, if s1 = s2, then we have 0-0 = 0, if we have s1< s2, then 0-1 = -1.
    return (s1 > s2) - (s1 < s2)

version1 = "1.0.3"
version2 = "1.0.7"

ans = compareVersion(version1, version2)
if ans < 0:
    print version1 + " is smaller"
elif ans > 0:
    print version2 + " is smaller"
else:
    print "Both versions are equal"

# Complexity: time complexity is O(n+m), where n and m are lengths of our strings, space complexity O(n+m) as well.
