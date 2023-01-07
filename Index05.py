def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    sum = 0
    for n in s:
        if n.isdecimal() == 1:
            sum += 1
        else:
            sum += 0
    return sum


print(main('2 3 a s 4 s f 3 5'))
