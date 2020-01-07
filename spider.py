#!/usr/bin/python3
import sys
import argparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="the url to crawl")
parser.add_argument("--recurse", help="recursively crawl dirs", action="store_true")
args = parser.parse_args()

if args.url is None:
    print("Specify a url to crawl with --url")
    sys.exit()

def crawl(url: str, already_crawled_urls: list):
    response = requests.request('GET', url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.findAll('a')
    for link in links:
        try:
            recursive_url = f"{url}/{link['href']}"
            if recursive_url in already_crawled_urls:
                continue
        except:
            continue
        print(recursive_url)
        already_crawled_urls.append(recursive_url)
        if recursive_url.endswith('/') and args.recurse is True:
            crawl(recursive_url[:-1], already_crawled_urls)

crawl(args.url, [])
