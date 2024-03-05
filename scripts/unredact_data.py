import argparse
import json
import praw
from tqdm import tqdm

# set up argparse to make the script easier to configure
parser = argparse.ArgumentParser()
parser.add_argument("in_file", help="file to unredact")
parser.add_argument("out_file", help="file to write to")
args = parser.parse_args()

# load in redacted data
with open(args.in_file, "r") as f:
    data = json.load(f)

# load in reddit keys and set up instance
with open("../private/reddit_private.json", "r") as f:
    reddit_private = json.load(f)

reddit = praw.Reddit(
    client_id=reddit_private["client_id"],
    client_secret=reddit_private["client_secret"],
    user_agent=reddit_private["user_agent"],
    username=reddit_private["username"],
    password=reddit_private["password"],
)

# get all ids from file and make list of fullnames
ids = [f"t1_{entry["comment_id"]}" for entry in data]

# use list of fullnaes to batch queries and populate dict that maps id to text
id_dict = {}
for c in tqdm(reddit.info(fullnames=ids), total=len(ids)):
    id_dict[c.id] = c.body

# use id to text dict to fill in data
for entry in data:
    entry["text"] = id_dict[entry["comment_id"]]

# write unredacted data
with open(args.out_file, "w") as f:
    json.dump(data, f, indent=4)
