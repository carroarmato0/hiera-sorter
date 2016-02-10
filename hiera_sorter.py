#!/usr/bin/python

import ruamel.yaml
from ruamel.yaml.comments import CommentedMap
import os.path
import argparse

class HieraSorter:
    def run(self):
        options = self.parse_args()
        self.start(options)


    def start(self, options):
        for file_path in options.files:
            self.sort_file(file_path)

    def sort_dict(self, initial_dict):
        result = []
        for k, v in sorted(initial_dict.iteritems()):
            if isinstance(v, CommentedMap):
                v = self.sort_dict(v)
            elif v is list:
                v = sorted(v)
            result.append((k,v))
        cm = CommentedMap(result)
        if hasattr(initial_dict, '_yaml_comment'):
            cm._yaml_comment = initial_dict._yaml_comment
        return cm

    def sort_file(self, file_path):
        if not os.path.isfile(file_path):
            raise Exception('%s is not a file' % file_path)
        with open(file_path, 'r') as stream:
            data = ruamel.yaml.load(stream, ruamel.yaml.RoundTripLoader)
        data = self.sort_dict(data)
        print ruamel.yaml.dump(data, Dumper=ruamel.yaml.RoundTripDumper),

    def parse_args(self):
        parser = argparse.ArgumentParser(description='Sort a YAML file, respecting its comments')
        parser.add_argument('files', metavar='file', nargs='+',
                            help='a file to be sorted')
        return parser.parse_args()


if __name__ == "__main__":
    HieraSorter().run()
