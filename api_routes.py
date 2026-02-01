import requests
def get_status_code(url):
    res = requests.get(url)
    return res.status_code

def test():
    print("this is test function")