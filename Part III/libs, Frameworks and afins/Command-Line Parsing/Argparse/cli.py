"""
from: https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/
"""
import argparse


def greet(args):
    output = '{0}, {1}!'.format(args.greeting, args.name)
    if args.caps:
        output = output.upper()
    print(output)

parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='1.0.0')
subparsers = parser.add_subparsers()

hello_parser = subparsers.add_parser('hello')
hello_parser.add_argument('name', help='name of the person to greet')
hello_parser.add_argument('--greeting', default='Hello',
                            help='word to use for the greeting')
hello_parser.add_argument('--caps', action='store_true',
                            help='uppercase the output')
hello_parser.set_defaults(func=greet)

goodbye_parser = subparsers.add_parser('goodbye')
goodbye_parser.add_argument('name', help='name of the person to greet')
goodbye_parser.add_argument('--greeting', default='Hello',
                            help='word to use for the greeting')
goodbye_parser.add_argument('--caps', action='store_true',
                            help='uppercase the output')
goodbye_parser.set_defaults(func=greet)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
