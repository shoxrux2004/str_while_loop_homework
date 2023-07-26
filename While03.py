def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sanoq=0
    i=0
    m=len(s)
    while i<m:
        if (s[i].isalpha()==False and s[i].isdigit()==False):
            sanoq+=1
        i+=1
    return sanoq
print(main("#hash77tag@$"))