def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    raqam=len(s)
    son=int(s)
    i=0
    sanoq=0
    while i<raqam:
        r=son%10
        if r%2==0:
            sanoq+=1
        i+=1
        son//=10
    return sanoq
print(main("56786543250"))