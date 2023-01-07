def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    number = int(s)
    n1 = number % 10
    number //= 10
    n2 = number % 10
    number //= 10
    n3 = number % 10
    number //= 10
    n4 = number % 10
    number //= 10
    n5 = number % 10
    return n1 + n2 + n3+n4 + n5


print(main('11111'))
