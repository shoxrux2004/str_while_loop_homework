def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sanoq=0
    i=0
    m=len(s)
    while i<m:
        if s[i].islower()==True:
            sanoq+=1
        i+=1
    return sanoq
print(main("CodeschoolUz"))