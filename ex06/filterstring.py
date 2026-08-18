from ft_filter import ft_filter
import sys

def main():
    try:
        n = int(sys.argv[2])
        filterString = lambda s : len(s) > n
        if len(sys.argv) != 3:
            print("AssertionError: the arguments are bad")
        else:
            res = sys.argv[1].split()
            res2 = list(filter(filterString , res))
            print(res2)
    except:
        print("AssertionError: the arguments are bad")

if __name__ == "__main__":
    main()