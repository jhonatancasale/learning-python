"""usage: greet [--help] <command> [<args>...]

options:
    -h --help         Show this screen.
    --version         Show the version.

commands:
    hello       Say hello
    goodbye     Say goodbye

"""

from docopt import docopt
from schema import Schema, SchemaError, Optional

HELLO = """usage: basic.py hello [options] [<name>]

    -h --help         Show this screen.
    --caps            Uppercase the output.
    --greeting=<str>  Greeting to use [default: Hello].
"""

GOODBYE = """usage: basic.py goodbye [options] [<name>]

    -h --help         Show this screen.
    --caps            Uppercase the output.
    --greeting=<str>  Greeting to use [default: Goodbye].
"""

"""
from: https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/
"""

def greet(args):
    output = '{0}, {1}!'.format(args['--greeting'], args['<name>'])
    if args['--caps']:
        output = output.upper()
    print(output)


if __name__ == '__main__':
    arguments = docopt(__doc__, options_first=True, version='1.0.0')

    schema = Schema({
        Optional('hello'): bool,
        Optional('goodbye'): bool,
        '<name>': str,
        Optional('--caps'): bool,
        Optional('--help'): bool,
        Optional('--greeting'): str
    })

    def validate(args): 
        try:
            args = schema.validate(args)
            return args

        except SchemaError as e:
            exit(e)

    if arguments['<command>'] == 'hello':
        greet(validate(docopt(HELLO)))
    elif arguments['<command>'] == 'goodbye':
        greet(validate(docopt(GOODBYE)))
    else:
        exit("{0} is not a command.  See 'options.py --help'.".format(arguments['<command>']))
