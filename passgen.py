import string
import random
import sys

passwd = ""
count = 1
mode = 0
length = 0


def print_help():
    print("Usage: python passgen.py -m [mode] -l [length]")
    print("Modes: 0 - digits only")
    print("       1 - letters only")
    print("       2 - alfanumeric")
    print("       3 - alfanumeric + symbols")


def error_handler():
    print_help()
    exit(1)


if len(sys.argv) > 2:
    while count < len(sys.argv):
        cmd = sys.argv[count]
        # Checking for -m flag and setting the mode
        if cmd == "-m":
            try:
                mode = int(sys.argv[count + 1])
                count += 2
                # print(f"Mode set to {mode}")
            except ValueError:
                error_handler()
        # Checking for -l flag and setting the length
        elif cmd == "-l":
            try:
                length = int(sys.argv[count + 1])
                count += 2
                # print(f"Length set to {length}")
            except ValueError:
                error_handler()
        # Printing help message
        elif cmd == "-h":
            print_help()
            exit(0)
    # Generating password made of digits
    if mode == 0:
        for i in range(length):
            passwd += random.choice(string.digits)
    # Generating password made of letters
    elif mode == 1:
        for i in range(length):
            passwd += random.choice(string.ascii_letters)
    # Generating password made of alfanumeric characters
    elif mode == 2:
        for i in range(length):
            passwd += random.choice(string.ascii_letters + string.digits)
    # Generatic password made of alfanumeric characters + symbols
    elif mode == 3:
        for i in range(length):
            passwd += random.choice(string.printable[:-7])

    print(f"Your randomly generated password is: {passwd}")

else:
    error_handler()
