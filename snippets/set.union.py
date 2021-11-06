def main() -> None:
    s = set("Test")

    print(s.union("Another"))
    #{'n', 'r', 'o', 'h', 's', 'T', 'A', 'e', 't'}

    print(s.union(set(['T', 'e', 's', 't'])))
    #{'s', 'T', 'e', 't'}

    print(s.union(['T', 'E', 'S', 'B']))
    #{'B', 's', 'S', 'T', 'E', 'e', 't'}

    # immutable!
    print(s.union("Another"))
    #{'n', 'r', 'o', 'h', 's', 'T', 'A', 'e', 't'}

    print(s.union(enumerate(['T', 'e', 's', 't'])))
    #{(1, 'e'), (2, 's'), (3, 't'), (0, 'T'), 's', 'T', 'e', 't'}

    print(s.union({"Test":1}))
    #{'s', 'T', 'Test', 'e', 't'}

    print(s | set("Test"))
    #{'s', 'T', 'e', 't'}


if __name__ == '__main__':
    print()

    main()
