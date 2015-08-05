import argparse


# read file and print in default ten lines
def read_file(file_name, line_number=10):
    with open(file_name) as f:
        temp = f.read().splitlines()
        if line_number > len(temp):
            line_number = len(temp)

        for i in range(0, line_number):
            print temp[i]


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
