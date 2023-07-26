def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
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
            sanoq+=1
        i+=1
        son//=10
    return sanoq
print(main("1567534"))