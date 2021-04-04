#!/usr/bin/env python
import argparse
import json
import logging
import os
import sys

OS_TYPES = ['linux', 'windows', 'splunk']
WORKDIR = os.getcwd()

logging.basicConfig(format='%(asctime)s %(threadName)s %(levelname)s %(message)s', level=logging.INFO)


def parse(key, data):
    output = []
    if type(data) is not list:
        data = [data]
    for d in data:
        try:
            output.append(d[key]['storageProfile']['osDisk']['managedDisk']['id'])
        except KeyError:
            continue
    return output

def main():
    parser = argparse.ArgumentParser(description='JSON parser')
    parser.add_argument('-i', '--input', help='filename', required=True)
    parser.add_argument('-s', '--string', choices=OS_TYPES, help='os type', required=True)
    args = parser.parse_args()

    input_path = os.path.join(WORKDIR, args.input)
    try:
        with open(input_path) as f:
            match = parse(args.string, json.load(f))
            if match:
                for m in match:
                    print(m)
    except IOError:
        print('File not found in working directory: {}'.format(args.input))
        sys.exit(1)
    except ValueError:
        print('File not valid JSON: {}'.format(args.input))
        sys.exit(1)
    except Exception as e:
        logging.exception(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
