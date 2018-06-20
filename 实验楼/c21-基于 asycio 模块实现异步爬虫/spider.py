#!/usr/bin/env python3

import time
import aiohttp
import asyncio
import async_timeout
import csv
from scrapy.http import HtmlResponse

results = []

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def task(url):
    async with aiohttp.ClientSession() as session:
         body =await fetch(session, url)
         parse(url, body)

def parse(url, body):
    response = HtmlResponse(url=url, body=body, encoding=('utf-8'))
    for repo in response.css('li[itemprop=owns]'):
        item = []
        item.append(repo.css('a[itemprop~="name"]::text').extract_first().strip())
        item.append(repo.css('relative-time::attr(datetime)').extract_first())
        results.append(item)


def main():
    t0 = time.time()
    loop = asyncio.get_event_loop()
    url_template = 'https://github.com/shiyanlou?page={}&tab=repositories'
    tasks = [task(url_template.format(i)) for i in range(1,5)]
    loop.run_until_complete(asyncio.gather(*tasks))
    with open('/home/shiyanlou/shiyanlou-repos.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)
    print(time.time()-t0)


if __name__ == '__main__':
    
    main()





