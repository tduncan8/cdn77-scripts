import argparse
import requests
import sys
parser = argparse.ArgumentParser()

parser.add_argument("--zone", help="cdn77 zone id", type=int, required=True)
parser.add_argument("--token", help="cdn77 api token", type=str, required=True)
parser.add_argument("--file", help=" relative file to purge from cache", type=str, required=True)

# check for no arguments entered and print help and exit.
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(0)

args = parser.parse_args()
zone = args.zone
url = f"https://api.cdn77.com/v3/cdn/{zone}/job/purge"
print(f"- Interacting with zone url: {url}")

