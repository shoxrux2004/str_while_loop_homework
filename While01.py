def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    m = len(s)
    i = 0
    sanoq = 0
    while i < m:
        if s[i].isdigit() == True:
            sanoq += 1
        i += 1
    return 
print(main("python 2023"))