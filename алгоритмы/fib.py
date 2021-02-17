def fib(n):
    # put your code here
    if n == 1:
        return 0
    if n == 2:
        return 1
    if 1 <= n and n <= 40:
        return fib(n - 1) + fib(n - 2)


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()