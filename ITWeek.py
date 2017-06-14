import requests
from bs4 import BeautifulSoup
import re

def main():
    url = 'https://ex-portal3.reed.jp/list/SODECS2017_ja.html'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    companies = soup.find_all('tr')
    pattern = r"�g���݃V�X�e���J���Z�p�W"
    print("�g���݃V�X�e���J���Z�p�W �ꗗ")
    print("��Ж� - �u�[�X�ԍ�")
    for company in companies:
        matchOB = re.search(pattern , company.text)
        if matchOB:
            name = company.find('td',class_="td_name")
            numb = company.find('td',class_="td_number")
            print_text = name.text + " - " + numb.text
            print(print_text)

if __name__ == '__main__':
    main()
