import argparse
import requests
parser = argparse.ArgumentParser()

parser.add_argument("-z","--zone", help="cdn77 zone id")
parser.add_argument("-t","--token", help="cdn77 api token")
parser.add_argument("-f","--file", help="file to purge from cache")
args = parser.parse_args()

