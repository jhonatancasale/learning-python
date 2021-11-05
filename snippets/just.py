def main() -> None:
    string: str = 'test'
    length: int = 10

    print()
    print(string.ljust(length, '-'))
    print(string.rjust(length, '-'))
    print(string.center(length, '-'))

if __name__ == '__main__':
    main()
