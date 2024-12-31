import argparse
import requests
import sys
parser = argparse.ArgumentParser()

parser.add_argument("--zone", help="cdn77 zone id")
parser.add_argument("--token", help="cdn77 api token")
parser.add_argument("--file", help="file to purge from cache")

# check for no arguments entered and print help and exit.
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(0)

args = parser.parse_args()

