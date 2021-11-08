def main() -> None:
    remove()
    discard()
    pop()

def remove() -> None:
    """
    <set>.remove does remove an arbitrary element x from <set>.
    It raises a KeyError if the x element was not present in the set
    """
    print()

    s = set(range(10))
    print(s)

    s.remove(5)
    print(s)

    result = s.remove(4)
    print(f"Result: {result}")
    print(s)

    try:
        s.remove(-10)
    except KeyError as error:
        print(f"Received error: {error}")
    else:
        print("Else Means -- No Exception")
    finally:
        print("Finally")

def discard() -> None:
    """
    <set>.discard does remove an arbitrary element x from <set>.
    It DOES NOT raise a KeyError if the x element was not present in the set
    """
    print()

    s = set(range(10))
    print(s)

    s.discard(5)
    print(s)

    result = s.discard(4)
    print(f"Result: {result}")
    print(s)

    try:
        s.discard(-10)
    except KeyError as error:
        print(f"Received error: {error}")
    else:
        print("Else Means -- No Exception")
    finally:
        print("Finally")

def pop() -> None:
    """
    <set>.pop does remove an arbitrary element from <set> ( and we can't choose.
    It raises a KeyError if there are no elements to remove
    """
    print()

    s = set(range(10))
    print(s)

    s.pop()
    print(s)

    result = s.pop()
    print(f"Result: {result}")
    print(s)

    s = set()
    try:
        s.pop()
    except KeyError as error:
        print(f"Received error: {error}")
    else:
        print("Else Means -- No Exception")
    finally:
        print("Finally")


if __name__ == '__main__':
    main()
