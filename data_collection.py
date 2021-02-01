import requests
import urllib3
urllib3.disable_warnings()
from datetime import date
import csv
import time
from bs4 import BeautifulSoup

data = []
dir = './data/'
iframe_src = 'https://connect2concepts.com/connect2/?type=circle&key=f7a11dda-3d6d-40d6-881b-8e4f6aabb56f'
today = date.today()


csvfile = open(dir+'data.csv', mode='w', newline='')
file = csv.writer(csvfile, delimiter=',')
file.writerow(['Location', 'Count', 'Percentage', 'Date', 'Time'])

while (True):
    s = requests.Session()
    http = urllib3.PoolManager()
    response = http.request('GET', iframe_src)
    soup = BeautifulSoup(response.data, 'html.parser')
    centers = soup.findAll("center")

    for center in centers:
        # print (center.contents)
        for content in center.contents[1:]:
            if '\n' not in content:
                if len(content) == 0:
                    # print (len(content), content)
                    # print (content.attrs)
                    _percentage = (content['data-percent'])
                if len(content) > 1:
                    # print (len(content), content)
                    # print (content.attrs, content.text)
                    extract = content.text.split('Last Count:')
                    temp = extract[1].split('Updated:')[1].split(" ", 2)
                    _count = extract[1].split('Updated:')[0]
                    _date = temp[1]
                    _time = temp[2]
                    _loc_name =  extract[0]
                    # _count = extract[1][:2]
                    print (extract, temp)
                    print (_loc_name, _count, _percentage, _date, _time)
                    file.writerow([_loc_name, _count, _percentage, _date, _time])
                    csvfile.flush()
    time.sleep(60)
