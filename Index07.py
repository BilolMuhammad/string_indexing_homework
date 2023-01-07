def main(s, n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    n -= 1
    if len(s) >= n:
        return s[n]
    else:
        return False


print(main('sdfg', 3))
