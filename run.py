import requests

url = 'https://panel.ct8.pl/login/'
username = 'iytest'
password = 'Tsglockey!1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
data = {
    'user': username,
    'pass': password,
}

response = requests.post(url, headers = {'user-agent': 'anything'}, data=data)
if response.status_code == 200:
    print("Successfully logged in as {username}".format(username=username))
else:
    print("Login unsuccessful: HTTP/{status_code}".format(status_code=response.status_code))
