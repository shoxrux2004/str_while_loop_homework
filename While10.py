def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sanoq=0
    i=0
    m=len(s)
    son=int(s)
    while i<m:
        r=son%10
        if(r%2==1):
            sanoq+=r
        i+=1
        son//=10
    return sanoq
print(main("589765"))