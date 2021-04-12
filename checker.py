import autologin
import fo
def checker():
    address = "110.172.55.126"
    res = fo.ping(address)
    #print(res)
    if res==0:
        address = "www.google.co.in"
        res = fo.ping(address)
        while res!=0:
            autologin.autologin()
            import time
            res = fo.ping(address)
            print(res)
            time.sleep(5)
    return True

flag=checker()
while flag:
    import time
    time.sleep(5)
    flag=checker()