#!/usr/bin/python

import sys
import os.path
import argparse

class HieraSorter:
    def run(self):
        options = self.parse_args()
        self.start(options)


    def start(self, options):
        for file_path in options.files:
            self.sort_file(file_path)

    def sort_file(self, file_path):
        if not os.path.isfile(file_path):
            raise Exception('%s is not a file' % file_path)

    def parse_args(self):
        parser = argparse.ArgumentParser(description='Sort a YAML file, respecting its comments')
        parser.add_argument('files', metavar='file', nargs='+',
                            help='a file to be sorted')
        return parser.parse_args()


if __name__ == "__main__":
    HieraSorter().run()
