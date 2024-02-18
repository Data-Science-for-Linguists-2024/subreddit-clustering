import json
import os
import praw
from tqdm import tqdm  # progress bar since this will take a while

with open("../private/reddit_private.json", "r") as f:
    reddit_private = json.load(f)

with open("../private/top_subreddits.txt", "r") as f:
    sub_list = f.read().split()

# use existing comment data if it exists
# this is so i don't have to rerun the script in its entirety if i have to stop it unexpectedly
comment_data = {}
if os.path.exists("../private/comment_data.json"):
    with open("../private/comment_data.json", "r") as f:
        comment_data = json.load(f)

reddit = praw.Reddit(
    client_id=reddit_private["client_id"],
    client_secret=reddit_private["client_secret"],
    user_agent=reddit_private["user_agent"],
    username=reddit_private["username"],
    password=reddit_private["password"],
)

for sub_name in tqdm(sub_list, position=0):
    # skip over ones that were scrapped in a previous session
    if sub_name in comment_data:
        continue

    # grab the top 10 posts of the past year
    num_posts = 10
    posts = reddit.subreddit(sub_name).top(limit=num_posts, time_filter="year")

    comments = []
    for post in tqdm(posts, position=1, leave=False, total=num_posts, desc=f"r/{sub_name}"):
        # get rid of the weird non-comment objects
        post.comments.replace_more(limit=0)
        # this only gets top level comments
        # also ignores automoderator since it tends to leave the same comment on every post and i don't want that in my data
        comments.extend(
            [comment.body for comment in post.comments if comment.author != "AutoModerator"])

    comment_data[sub_name] = comments

    # save per iteration just to be safe
    with open("../private/comment_data.json", "w") as f:
        json.dump(comment_data, f)
