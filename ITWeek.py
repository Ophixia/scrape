import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://ex-portal3.reed.jp/list/SODECS2017_ja.html'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    companies = soup.find_all('tr')
    for company in companies:
        print(company.text)

if __name__ == '__main__':
    main()

