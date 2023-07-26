def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
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
        sanoq+=r
        i+=1
        son//=10
    return sanoq
print(main("987654"))
    