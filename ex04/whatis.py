import sys

if len(sys.argv) != 2 and len(sys.argv) != 1:
    print("AssertionError: argument is not an integer")
elif len(sys.argv) != 1 and int(sys.argv[1]) % 2 == 0:
    print("I'm Even.")
elif len(sys.argv) != 1 and int(sys.argv[1]) % 2 != 0:
    print("I'm Odd.")
 