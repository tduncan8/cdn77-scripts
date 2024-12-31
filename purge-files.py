import argparse
import requests
import sys
import json
parser = argparse.ArgumentParser()

parser.add_argument("--zone", help="cdn77 zone id", type=int, required=True)
parser.add_argument("--token", help="cdn77 api token", type=str, required=True)
parser.add_argument("--file", help="Relative files to purge from cache (space-separated list)",nargs='+', type=str, required=True)

# check for no arguments entered and print help and exit.
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(0)

args = parser.parse_args()
zone = args.zone
file = args.file
auth_token = args.token
data = {'paths' : file}
headers = {'Authorization': f"Bearer {auth_token}"}
url = f"https://api.cdn77.com/v3/cdn/{zone}/job/purge"

print(f"Submitting payload to zone url: {url}")

def purge_file(url, data, headers):
    try:
      response = requests.post(url, json=data, headers=headers)
      response.raise_for_status()
      return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


purge_results = purge_file(url,data,headers)
if purge_results:
    try:
      output = purge_results.json()
      print(f"Job Submission Results:")
      print("ID:", output["id"])
      print("State:", output["state"])
      print("Started:", output["queued_at"])
      print("Paths:", output["paths"])
    except ValueError:
        print("Error: The response could not be parsed as JSON.")
else:
 print('purge request failed')
