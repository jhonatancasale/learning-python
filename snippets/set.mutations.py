def main() -> None:
    union()
    intersection()
    difference()
    symmetric_difference()


def union() -> None:
    A = set(range(10))
    B = set(_ for _ in range(15) if _ % 2)

    print()

    print(f"A: {A}")
    print(f"B: {B}")

    A = set(range(10))
    print(f"A: {A}")
    print(f"{A}.update({B}) = ", end="")
    A.update(B)
    print(A)

    A = set(range(10))
    print(f"A: {A}")
    print(f"{A} |= {B} = ", end="")
    A |= B
    print(A)


def intersection() -> None:
    A = set(range(10))
    B = set(_ for _ in range(15) if _ % 2)

    print()

    print(f"A: {A}")
    print(f"B: {B}")

    A = set(range(10))
    print(f"A: {A}")
    print(f"{A}.intersection_update({B}) = ", end="")
    A.intersection_update(B)
    print(A)

    A = set(range(10))
    print(f"A: {A}")
    print(f"{A} &= {B} = ", end="")
    A &= B
    print(A)


def difference() -> None:
    A = set(range(10))
    B = set(_ for _ in range(15) if _ % 2)

    print()

    print(f"A: {A}")
    print(f"B: {B}")

    A = set(range(10))
    print(f"A: {A}")
    print(f"{A}.difference_update({B}) = ", end="")
    A.difference_update(B)
    print(A)

    A = set(range(10))
    print(f"A: {A}")
    print(f"{A} -= {B} = ", end="")
    A -= B
    print(A)


def symmetric_difference() -> None:
    A = set(range(10))
    B = set(_ for _ in range(15) if _ % 2)

    print()

    print(f"A: {A}")
    print(f"B: {B}")

    A = set(range(10))
    print(f"A: {A}")
    print(f"{A}.symmetric_difference_update({B}) = ", end="")
    A.symmetric_difference_update(B)
    print(A)

    A = set(range(10))
    print(f"A: {A}")
    print(f"{A} ^= {B} = ", end="")
    A ^= B
    print(A)


if __name__ == "__main__":
    main()
