import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='List contents of directory.')
    parser.add_argument('path', nargs='?', type=str, help='the parent directory', default=None)
    return parser.parse_args()


def os_walk(start_directory):
    for root, dirs, files in os.walk(start_directory, topdown=True):
        for name in files:
            print(os.path.join(root, name))


def valid_args(argparse_args):
    if argparse_args.path and os.path.exists(argparse_args.path):
        return True
    else:
        return False


if __name__ == '__main__':
    args = parse_args()
    if valid_args(args):
        os_walk(args.path)
    else:
        print("Directory is not specified")
