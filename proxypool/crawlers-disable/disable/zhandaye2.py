from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler


BASE_URL = 'https://www.zdaye.com/free/{page}/'
MAX_PAGE = 5


class ZhandayeCrawler(BaseCrawler):
    """
    crawler, https://www.zdaye.com/free/1/
    """
    urls = [BASE_URL.format(page=page) for page in range(1, MAX_PAGE + 1)]
    
    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        trs = doc('#ipc tr:gt(0)').items()
        for tr in trs:
            if not tr.find('td:nth-child(6)').html().__contains__("iyes"):
                host = tr.find('td:nth-child(1)').text()
                port = int(tr.find('td:nth-child(2)').text())
                yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = ZhandayeCrawler()
    for proxy in crawler.crawl():
        print(proxy)
