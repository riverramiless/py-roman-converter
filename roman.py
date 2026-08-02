def roman_to_int(s):
    mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100}
    total = 0
    for i in range(len(s)):
        val = mapping.get(s[i], 0)