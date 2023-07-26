def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    sanoq=0
    i=0
    m=len(s)
    while i<m:
        if (s[i].isalpha()==True and s[i]!='a' and s[i]!='e' and s[i]!='i' and s[i]!='o' and s[i]!='u'):
            sanoq+=1
        i+=1
    return sanoq
print(main("abdseloni"))