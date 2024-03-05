import argparse
import json

# set up argparse to make the script easier to configure
parser = argparse.ArgumentParser()
parser.add_argument("in_file", help="file to redact")
parser.add_argument("out_file", help="file to write to")

args = parser.parse_args()

# read json file
with open(args.in_file, "r") as f:
    data = json.load(f)

# blank out text field
for entry in data:
    entry["text"] = ""

# write json file
with open(args.out_file, "w") as f:
    json.dump(data, f, indent=4)
