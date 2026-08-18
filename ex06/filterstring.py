from ft_filter import ft_filter
import sys

if len(sys.argv) != 3:
n = int(sys.argv[2])
filterString = lambda s : len(s) > n


def main():
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
    else:
        res = sys.argv[1].split()
        to = filter(filterString , res)
        for i in to:
                print (i)

if __name__ == "__main__":
    main()