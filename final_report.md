# Subreddit Clustering
by Madeline Powers

## Introduction
Reddit is a fascinating source of linguistic data. It provides a vast number of posts and comments, all already organized into subreddits by topic. This project aims to further examine this topic grouping, by trying to further group subreddits by topic, and analyze their content by using topic modeling techniques.

## Data Collection
Instead of using a preexisting dataset, I decided to collect my own. To start, I needed a list of subreddits to scrape from. The most comprehensive list I could find online was reddit's own [Top Communities](https://www.reddit.com/best/communities/1/) page. Strangly, this list doesn't include every subreddit, r/AmItheAsshole for example is excluded. Unfortunately I couldn't find a better list with this many subreddits, so it's what I used. [`scrape_top_comments.py`](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/blob/main/scripts/scrape_top_subreddits.py) scrapes this list using beautifulsoup and writes it to a file. This was the list I used for my next step.

The next step was scraping text from reddit. I decided to specifically use comments, as some subreddits only allow image posts, but (nearly) every subreddit allows comments. This removes any bias that might come from not including image based subreddits. To scrape the comments, I used [PRAW](https://praw.readthedocs.io/en/stable/), a python wrapper for the reddit api. [`scrape_comments.py`](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/blob/main/scripts/scrape_comments.py) uses PRAW and the list of subreddits to get all comments for the top 10 most upvoted posts of the past year. This script took a very long time to run due to reddit's rate limits, which were recently reduced. I had to leave my computer on overnight twice, but ended up with a very good dataset.

Another big problem with this dataset was sharing it. To my knowledge, reddit doesn't like people publishing large amounts of text obtained using their API. To get around this, I took inspiration from the [GUM corpus](https://github.com/amir-zeldes/gum). My published data is the same as the full dataset, but with the `text` field removed using [`redact_data.py`](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/blob/main/scripts/redact_data.py). Using the `comment_id` field and the reddit api, the text can be retrieved to reconstruct the whole dataset using [`unredact_data.py`](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/blob/main/scripts/unredact_data.py).

## Data cleanup and exploration


## Analysis

## Difficulties

## Conclusion
