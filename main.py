from sum import add
from difference import subtract
from product import multiply


def main() -> None:
    a = 10
    b = 5
    print(f"sum: {add(a, b)}")
    print(f"difference: {subtract(a, b)}")
    print(f"product: {multiply(a, b)}")


if __name__ == "__main__":
    main()
