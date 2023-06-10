from lib.ArgParser import get_args
from lib.Parser import Parser


def main():
    args = get_args()
    parser = Parser(args)
    parser.parse()


if __name__ == '__main__':
    main()
