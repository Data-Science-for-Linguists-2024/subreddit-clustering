import argparse
from bs4 import BeautifulSoup
import requests

parser = argparse.ArgumentParser()
parser.add_argument("num_pages", type=int, help="number of pages to scrape, 250 per page")
parser.add_argument("-o", dest="output", help="output file")
args = parser.parse_args()

result = []
for i in range(1, args.num_pages + 1):
    page = requests.get(f"https://www.reddit.com/best/communities/{i}/")
    soup = BeautifulSoup(page.text, features="html.parser")
    sub_list = soup.find_all("div", {"class": "community-list"})
    result.extend([link.get_text().strip() for link in sub_list[0].findChildren("a")])

if args.output is None:
    print("\n".join(result))
else:
    with open(args.output, "w", newline="\n") as f:
        f.write("\n".join(result))
