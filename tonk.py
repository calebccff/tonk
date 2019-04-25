#!/usr/bin/env python

import toml, argparse
from trello import TrelloClient

FORMAT_RESET = '${color white}'
FORMAT_CHECKLIST = '${color 36648B}'
FORMAT_TASK = '${color D62D20}'
FORMAT_SUBTASK = '${color 900020}'
FORMAT_SUBTASK_DONE = '${color BEF6C7}'

CONFIG = "$HOME/.config/tonk"


parser = argparse.ArgumentParser(description='Update conky to show your TODO list')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('-c', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print args.accumulate(args.integers)

if __name__ == "__main__":
    main()