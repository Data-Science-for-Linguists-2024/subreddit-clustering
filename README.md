# subreddit-clustering
Madeline Powers, hap60@pitt.edu, April 28, 2024

## Project description
This repository contains an analysis of the topics of subreddits using topic modeling with scikit learn on a large dataset of reddit comments.

## Data description
The data used for this project was collected specifically for it, using [PRAW](https://praw.readthedocs.io/en/stable/). It is included in the repository in partial form, and can be reconstructed using the [unredact_data.py](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/blob/main/scripts/unredact_data.py) script.

## Directory
- **[final_report.md](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/blob/main/final_report.md): Final report for the project.**
- [data/](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/tree/main/data): directory containing partial data files, used for data reconstructin
- [data_samples/](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/tree/main/data_samples): directory containing samples of the full data
- [images/](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/tree/main/images): directory containing plot images
- [notebooks/](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/tree/main/notebooks): directory for jupyter notebooks
    - [data_exploration.ipynb](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/blob/main/notebooks/data_exploration.ipynb): initial exploration and cleanup of data
    - [clustering.ipynb](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/blob/main/notebooks/clustering.ipynb): document clustering and analysis
- [scripts/](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/tree/main/scripts): directory for python scripts
    - [scrape_top_subreddits.py](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/blob/main/scripts/scrape_top_subreddits.py): script for gathering a list of the top n subreddits
    - [scrape_comments.py](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/blob/main/scripts/scrape_comments.py): script for scraping comments from reddit
    - [redact_data.py](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/blob/main/scripts/redact_data.py): script to produce the partial data files
    - [unredact_data.py](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/blob/main/scripts/unredact_data.py): script to reconstruct dataset
- [presentation.pdf](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/blob/main/presentation.pdf): presentation given in class
- [progress_report.md](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/blob/main/progress_report.md): progress reports written during the project
- [project_plan.md](https://github.com/Data-Science-for-Linguists-2024/subreddit-clustering/blob/main/project_plan.md): initial plan for project

## Guestbook
[guestbook for fellow students](https://github.com/Data-Science-for-Linguists-2024/Class-Lounge/blob/main/guestbooks/maddy.md)
