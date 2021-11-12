from collections import defaultdict


def main() -> None:
    print()

    default_dict = defaultdict(lambda: "Maybe I missed something?")
    default_dict['a'] = 1
    default_dict['b'] = 2
    
    print(default_dict['a'])
    print(default_dict['b'])
    print(default_dict['c'])


if __name__ == '__main__':
    main()
