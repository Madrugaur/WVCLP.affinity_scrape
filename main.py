from pip._vendor import requests
from bs4 import BeautifulSoup
status_map = {
    'This space is currently full.Please do not enter.': 0,
    'This space is nearing capacity.': 1,
    'Space is available, come on in!': 2
}

for i in range(1, 5):
    html_text = requests.get("http://rfidaccesscontrol.azurewebsites.net/Capacity/Sign/" + str(i)).text
    soup = BeautifulSoup(html_text, "html.parser")
    title = soup.find("title").text
    status = soup.find(id="resultarea").text.replace("\n", "")
    print(title, ": ", status, " => CODE ", status_map[status], sep="")

