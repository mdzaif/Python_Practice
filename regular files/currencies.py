import requests
from bs4 import BeautifulSoup
import sys
import csv

def cal(amt, cur1, cur2):
    
    def req(url):
        r = requests.get(url)
        rc = r.content
        s = BeautifulSoup(rc, 'html.parser')
        return s

    def info():
        url1 = req(f'https://www.xe.com/currencyconverter/convert/?Amount=2&From={cur1}&To={cur2}')
        q1 = url1.find_all('div', {'class' : 'sc-ac62c6d1-0 GwlFu'})
        q1 = str(q1)
        s = BeautifulSoup(q1, 'html.parser')
        q1 = s.find_all('p')
        for r in q1:
            print(r.text)
        print("The data collect from: https://xe.com")
        print('\n')


    if amt <= 0:
        print("Invalid ammount!")

    elif amt == 1:
        info()

    else:
        url = req(f'https://www.xe.com/currencyconverter/convert/?Amount={amt}&From={cur1}&To={cur2}')
        q2 = url.find_all('p', {'class' : 'sc-295edd9f-0 lfRgod'})
        q3 = url.find_all('p', {'class' : 'sc-295edd9f-1 jqMUXt'})
        s1 = s2 = ''
        for t,e in zip(q2, q3):
            s1 = t.text
            s2 = e.text
        s1 = s1 + ' ' + s2
        print(s1)
        print('\n-------------INFORMATION---------------\n')
        info()

def currency_check(cur):

    with open('currency.csv') as cur_iso:
        read = csv.DictReader(cur_iso)
        for rows in read:
            if rows['Currency ISO code'] == cur:
                return cur
    print(f"Invaild currency : {cur}")
    sys.exit(1)

if __name__ == "__main__":
    
    print('-----WELCOME TO CURRENCY CONVERTER ------------')
    amt = int(input("Ammount: ").strip())
    cur1 = currency_check(input("From: ").upper().strip())
    cur2 = currency_check(input("To: ").upper().strip())
    print('\n')
    print("------- Your Search Result --------------\n")
    cal(amt, cur1, cur2)
