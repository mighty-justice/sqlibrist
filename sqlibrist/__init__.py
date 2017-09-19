# -*- coding: utf8 -*-
VERSION = '0.1.10'

import sys

from sqlibrist.helpers import SqlibristException, handle_exception, \
    get_command_parser, LazyConfig


def main():
    parser = get_command_parser()
    args = parser.parse_args()
    config = LazyConfig(args)
    try:
        args.func(args, config)
    except SqlibristException as e:
        handle_exception(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
