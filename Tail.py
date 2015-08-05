# coding=utf-8
import argparse


# reading depending on the user' input
def read_file(file, line_length):
    with open(file) as f:
        temp = f.read().splitlines()
        if line_length > len(temp):
            line_length = len(temp)
        start_point = len(temp) - line_length
        for lines in range(start_point, len(temp)):
            print temp[lines]

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("file")
        parser.add_argument("-n", type=int)
        args = parser.parse_args()
        if args.file:
            if args.n:
                read_file(args.file, args.n)
            else:
                read_file(args.file)
    except ValueError:
        print("Please enter valid values!")
