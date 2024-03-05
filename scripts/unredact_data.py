import argparse
import json
import praw
from tqdm import tqdm

# set up argparse to make the script easier to configure
parser = argparse.ArgumentParser()
parser.add_argument("in_file", help="file to unredact")
parser.add_argument("out_file", help="file to write to")

args = parser.parse_args()

with open(args.in_file, "r") as f:
    data = json.load(f)

with open("../private/reddit_private.json", "r") as f:
    reddit_private = json.load(f)

reddit = praw.Reddit(
    client_id=reddit_private["client_id"],
    client_secret=reddit_private["client_secret"],
    user_agent=reddit_private["user_agent"],
    username=reddit_private["username"],
    password=reddit_private["password"],
)

ids = [f"t1_{entry["comment_id"]}" for entry in data]

id_dict = {}
for c in tqdm(reddit.info(fullnames=ids), total=len(ids)):
    id_dict[c.id] = c.body

for entry in data:
    entry["text"] = id_dict[entry["comment_id"]]

with open(args.out_file, "w") as f:
    json.dump(data, f, indent=4)
