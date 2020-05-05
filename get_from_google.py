import requests as rq
import lxml
from bs4 import BeautifulSoup


def get_data(request: str, pageNo: int):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    url = 'https://www.google.com/search'
    payload = {'q': request, 'start': str(10 * pageNo), 'headers': headers}
    r = rq.get(url, payload)
    content = r.content
    soup = BeautifulSoup(content, features="lxml")

    for item in soup.select(".r a"):
        print(item.text)
    """
    # https://stackoverflow.com/questions/7746832/scraping-and-parsing-google-search-results-using-python
    
    for next_page in soup.select(".fl"):
        res = rq.get(base + next_page.get('href'))
        soup = BeautifulSoup(res.text, "lxml")
        for item in soup.select(".r a"):
            print(item.text)

"""

    alls = []

    for d in soup.findAll('div', attrs={'class': 'rc'}):
        # print(d)
        name = d.find('div', attrs={'class': 'r'})
        n = d.find('a', alt=True)
        if n and len(n.attrs):
            print('> ', n.text, ': ', n.attrs['href'])
        description = d.find('span', attrs={'class': 'st'})

        all1 = []

        if name is not None:
            # print(n[0]['alt'])
            all1.append(n[0]['alt'])
        else:
            all1.append("unknown-product")

        if description is not None:
            print(description.text)
            all1.append(description.text)
        else:
            all1.append('-1')

    return alls
