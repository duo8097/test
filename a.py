import sys

def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    total = n * n + 3 * n + 1
    sys.stdout.write(str(total))

if __name__ == "__main__":
    main()
