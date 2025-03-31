def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i  # yield returns an iterator,
        #                 yield result after each iteration
        #                 NP print 1,000,000 sheep!  (c:


if __name__ == "__main__":
    main()
