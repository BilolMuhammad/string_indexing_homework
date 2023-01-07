def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    sum = 0
    for n in s:
        if n == '*':
            sum += 1
        else:
            sum += 0
    return sum


print(main('sd*sd*df'))
