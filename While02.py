def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    m=len(s)
    sanoq=0
    i=0
    while i<m:
        if s[i].isalpha()==True:
            sanoq+=1
        i+=1
    return sanoq
print(main("shoxrux 6974"))