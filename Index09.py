def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s >= '1' and s <= '9':
        return int(s)
    else:
        return False


print(main('5'))
