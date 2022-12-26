import requests

url = 'https://panel.ct8.pl/login/'
username = 'iytest'
password = 'Tsglockey!1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
}
data = {
    'user': username,
    'pass': password,
}

response = requests.post(url, headers=headers, data=data)
if response.status_code == 200:
    print "Successfully logged in as {username}".format(username=username)
else:
    print "Login unsuccessful: HTTP/{status_code}".format(status_code=response.status_code
