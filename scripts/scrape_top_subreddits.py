import argparse
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

# set up argparse to make the script easier to configure
parser = argparse.ArgumentParser()
parser.add_argument("num_pages", type=int,
                    help="number of pages to scrape, 250 per page")
parser.add_argument("-o", dest="output", help="output file")
args = parser.parse_args()


result = []
# loop through each page, add one since pages are 1 indexed
for i in tqdm(range(1, args.num_pages + 1)):
    # get page `i` of the top subreddit list`
    page = requests.get(f"https://www.reddit.com/best/communities/{i}/")

    # parse the page, find the list,
    # then get all the subreddit names from the link text stripping off the "r/" part
    soup = BeautifulSoup(page.text, features="html.parser")
    sub_list = soup.find_all("div", {"class": "community-list"})
    result.extend([link.get_text().strip().split("/")[1]
                  for link in sub_list[0].findChildren("a")])

# print if no output file supplied
if args.output is None:
    print("\n".join(result))
else:
    with open(args.output, "w", newline="\n") as f:
        f.write("\n".join(result))
