import os
import argparse
from collections import defaultdict


def parse_args():
    parser = argparse.ArgumentParser(description='List contents of directory.')
    parser.add_argument('path', nargs='?', type=str, help='the parent directory', default=None)
    return parser.parse_args()


def valid_args(argparse_args):
    if argparse_args.path and os.path.exists(argparse_args.path):
        return True
    else:
        return False


class Descending:

    def __str__(self):
        return "Descending"

    def __init__(self):
        self.reverse = True

    def sort(self, dictionary) -> list:
        return sorted(dictionary.keys(), reverse=self.reverse)


class Ascending:

    def __str__(self):
        return "Ascending"

    def __init__(self):
        self.reverse = False

    def sort(self, dictionary: defaultdict) -> list:
        return sorted(dictionary.keys(), reverse=self.reverse)


class FileSorter:

    sorting_options = {
        1: Descending(),
        2: Ascending()
    }

    def set_sorting_option(self, sorting_option):
        if sorting_option in self.sorting_options.keys():
            return self.sorting_options[sorting_option]
        return None

    def __init__(self):
        self.file_type = input("Enter file format:\n")

        print("Size sorting options:")
        for i, sorting_option in self.sorting_options.items():
            print(f"{i}. {sorting_option}")

        self.sorting_option = None
        while self.sorting_option is None:
            self.sorting_option = self.set_sorting_option(int(input("Enter a sorting option:\n")))
            if self.sorting_option is None:
                print("Wrong option")

    def os_walk(self, start_directory):
        file_dict = defaultdict(list)
        for root, dirs, files in os.walk(start_directory, topdown=True):
            for name in files:
                file_name = os.path.join(root, name)
                file_size = os.stat(file_name).st_size
                _, file_extension = os.path.splitext(file_name)

                if self.file_type == "" or self.file_type == file_extension[1:]:
                    file_dict[file_size].append(file_name)

        return file_dict


if __name__ == '__main__':
    args = parse_args()
    if valid_args(args):
        file_sorter = FileSorter()

        my_files = file_sorter.os_walk(args.path)
        sort_type = file_sorter.sorting_option

        sorted_keys = sort_type.sort(my_files)
        for key in sorted_keys:
            print(f"{key} bytes")
            for file in my_files[key]:
                print(file)
            print()

    else:
        print("Directory is not specified")
