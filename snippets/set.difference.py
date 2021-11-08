def main() -> None:
    s = set("Test")

    print(s.difference("Another"))
    print(s.difference(set(['a', 'b', 'c', 'd'])))
    print(s.difference(['a', 'b', 'c', 'd']))
    print(s.difference(enumerate(['a', 'b', 'c', 'd'])))
    print(s.difference({"Another":1}))
    print(s - set("Another"))


if __name__ == '__main__':
    main()


