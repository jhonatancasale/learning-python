from textwrap import wrap

def textwrap_wrap_example(string: str, piece_lenght: int) -> str:
    return '\n'.join(wrap(string, piece_lenght))

def main() -> None:
    string: str = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
    piece_lenght: int = 4

    print(textwrap_wrap_example(string, piece_lenght))
    print()
    print(textwrap_wrap_example(string, piece_lenght + 1))
    print()
    print(textwrap_wrap_example(string, piece_lenght * 2))

if __name__ == '__main__':
    main()
