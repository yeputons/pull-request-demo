#!/usr/bin/env python3
import sys


def main():
    num = int(sys.argv[1])
    if num == 0:
        print("Егор Суворов")
        print("yeputons")
    elif num == 1:
        print("Студент Раз")
        print("student-one")
    else:
        print("Unknown id: {}".format(num))
        sys.exit(1)


if __name__ == "__main__":
    main()
