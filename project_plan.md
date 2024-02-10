# Subreddit Clustering

## Summary
For my project, I will be clustering subreddits based on comments scraped from reddit. I want to discover
unusual links between subreddits based on the vocabulary used by their users. Reddit specifically seems like
a good target for this sort of analysis as subreddits tend to have specific memes and phrases associated with them,
which I suspect will allow groups of users to be tracked across subreddits.

## Data
I plan to collect data using [PRAW](https://github.com/praw-dev/praw), a python wrapper for the reddit api.
I haven't yet decided on an exact size, but something like the [top 1000 subreddits](https://www.reddit.com/best/communities/1/)
seems like a reasonable scope. For each subreddit in the list I compile, I will scrape comments from the top posts.
There will definitely be some data cleaning involved to remove stuff like links and possibly markdown formatting,
but both of those seem pretty achievable.

## Analysis
To analyze my data, I will use document clustering. I still need to do a bit more research into the specfics of the different algorithms,
but the general process is to use TF-IDF embeddings and then a clustering algorithm, such as k-means. After that, I want to investigate
the contents of each cluster and the factors that led them to be grouped, as well as do a lot of data visualization.

## Presentation
The presentation will contain a selection of interesting results, for example subreddits I didn't expect to be connects,
as well as an explanation of my methods and lots of graphs.
